"""Offline release checks. Run from any working directory with Python 3.12+."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / 'docs/english-edition'
MARKDOWN = MarkdownIt('commonmark', {'html': True}).enable('table')

def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'))

def sha256(path: Path) -> str:
    payload = path.read_bytes()
    if path.suffix in {'.md', '.svg', '.html'}:
        payload = payload.replace(b'\r\n', b'\n')
    return hashlib.sha256(payload).hexdigest()

@lru_cache(maxsize=256)
def source_text(path: str, commit: str) -> str:
    return subprocess.check_output(['git', 'show', f'{commit}:{path}'], cwd=ROOT).decode('utf-8-sig')

def content_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob('*') if p.suffix in {'.md','.html','.svg'} and '.git' not in p.parts)


def markdown_failures(files: list[Path]) -> list[str]:
    failures: list[str] = []
    for path in files:
        if path.suffix != '.md':
            continue
        raw = path.read_text(encoding='utf-8-sig')
        name = path.relative_to(ROOT).as_posix()
        tokens = MARKDOWN.parse(raw)
        for token in tokens:
            if token.type == 'fence' and token.map:
                last_line = raw.splitlines()[token.map[1] - 1].strip()
                if not last_line.startswith(token.markup):
                    failures.append(f'{name}: unclosed code fence')
        without_code = re.sub(r'`[^`\n]+`', '', raw)
        if len(re.findall(r'<details(?:\s[^>]*)?>', without_code)) != without_code.count('</details>'):
            failures.append(f'{name}: unbalanced expandable answers')
        if re.search(r'^#{1,6}\s+(?:README|Jigs|Iam)\s*$', raw, re.M):
            failures.append(f'{name}: untranslated or generic title')
    return failures


def source_integrity(inventory: dict[str, Any], audit: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    paths = subprocess.check_output(
        ['git', 'ls-tree', '-rz', '--name-only', inventory['source_commit']], cwd=ROOT,
    ).decode('utf-8').rstrip('\0').split('\0')
    original_paths = {row['original_path'] for row in inventory['files']}
    if set(paths) != original_paths:
        failures.append('inventory does not match the complete Portuguese source tree')
    for row in audit['questions']:
        if row.get('question_type') == 'open-response':
            continue
        source = source_text(row['original_source_path'], inventory['source_commit'])
        answers = re.findall(r'\*\*Resposta correta:\*\*\s*([A-D])', source)
        index = row['original_question_number'] - 1
        if index >= len(answers) or answers[index] != row['reviewed_answer']:
            failures.append(f'{row["stable_question_id"]}: original correct inline answer changed')
    return failures


def obsolete_path_failures(files: list[Path], inventory: dict[str, Any]) -> list[str]:
    old_paths = [row['original_path'] for row in inventory['files'] if row['original_path'] != row['target_path']]
    failures: list[str] = []
    for old in old_paths:
        if (ROOT / old).is_file():
            failures.append(f'obsolete Portuguese documentation remains: {old}')
    for path in files:
        if 'english-edition' in path.parts or path.suffix == '.html':
            continue
        raw = path.read_text(encoding='utf-8-sig')
        for old in old_paths:
            if old in raw and f'/main/{old}' not in raw:
                failures.append(f'{path.relative_to(ROOT)}: obsolete documentation path {old}')
    return failures

def slug(text: str) -> str:
    text = BeautifulSoup(MARKDOWN.renderInline(text), 'html.parser').get_text().lower()
    return re.sub(r'[^\w\- ]', '', text, flags=re.UNICODE).replace(' ', '-')

def anchors(path: Path) -> set[str]:
    text = path.read_text(encoding='utf-8-sig')
    found = set(re.findall(r'\bid=["\']([^"\']+)', text))
    duplicates: Counter[str] = Counter()
    for match in re.finditer(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        base = slug(match[1])
        suffix = f'-{duplicates[base]}' if duplicates[base] else ''
        found.add(base + suffix)
        duplicates[base] += 1
    return found

def link_failures(files: list[Path]) -> list[str]:
    failures = []
    for path in files:
        raw = path.read_text(encoding='utf-8-sig')
        rendered = MARKDOWN.render(raw) if path.suffix == '.md' else raw
        soup = BeautifulSoup(rendered, 'html.parser')
        for node in soup.select('[href], [src]'):
            href = str(node.get('href', node.get('src', '')))
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or href in {'','#'}:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(ROOT) or not target.exists():
                failures.append(f'{path.relative_to(ROOT)}: missing target {href}')
            elif parsed.fragment and target.suffix in {'.md','.html','.svg'}:
                if unquote(parsed.fragment) not in anchors(target):
                    failures.append(f'{path.relative_to(ROOT)}: missing anchor {href}')
    return failures

def question_failures(texts: dict[str,str], audit: dict[str,Any]) -> list[str]:
    failures = []
    actual: dict[str,tuple[str,str,int]] = {}
    for path,text in texts.items():
        matches = list(re.finditer(r'<!-- question-id: ([^;]+); domain: (\d); (.*?) -->',text))
        for i,match in enumerate(matches):
            qid = match[1]
            if qid in actual:
                failures.append(f'duplicate ID: {qid}')
            end = matches[i+1].start() if i+1 < len(matches) else len(text)
            actual[qid] = (path,text[match.end():end],int(match[2]))
    expected = {row['stable_question_id']:row for row in audit['questions']}
    if set(actual) != set(expected):
        failures.append(f'question ID coverage differs: {set(actual)^set(expected)}')
    numbered: dict[str,list[int]] = {}
    for qid,(path,block,domain) in actual.items():
        row = expected.get(qid)
        if row is None:
            continue
        if row['translated_target_path'] != path or domain != row['official_domain'] or domain not in {1,2,3,4}:
            failures.append(f'{qid}: path or domain differs from audit')
        if '<details>' not in block or '</details>' not in block:
            failures.append(f'{qid}: missing expandable answer')
        if row['official_aws_reference_url'] not in block:
            failures.append(f'{qid}: missing audited AWS reference')
        if row.get('question_type') == 'open-response':
            answer = re.search(r'\*\*Answer:\*\*\s*(.*?)</details>',block,re.S)
            if not answer or not answer[1].strip():
                failures.append(f'{qid}: missing open response')
            continue
        options = re.findall(r'^([A-D])\)\s+(.+)$',block,re.M)
        if [letter for letter,_ in options] != list('ABCD') or len({value.casefold() for _,value in options}) != 4:
            failures.append(f'{qid}: must have four distinct options A-D')
        answers = re.findall(r'\*\*Correct answer:\*\*\s*([A-D])\b',block)
        if answers != [row['reviewed_answer']]:
            failures.append(f'{qid}: inline answer differs from audit')
        for letter in 'ABCD':
            label = 'Correct' if letter == row['reviewed_answer'] else 'Incorrect'
            if f'**{letter} — {label}:**' not in block:
                failures.append(f'{qid}: missing or contradictory {letter} rationale')
        heading = re.search(r'^#{2,3} Question (\d+)',block,re.M)
        if not heading or int(heading[1]) != row['reviewed_question_number']:
            failures.append(f'{qid}: question number differs from audit')
        elif not qid.startswith('CLF-QUICK'):
            numbered.setdefault(path,[]).append(int(heading[1]))
        if path.startswith('16-') and not path.endswith('cross-domain-review-questions.md'):
            name = Path(path).name
            key_name = 'practice-exam-answer-key.md' if name == '10-question-practice-exam.md' else re.sub(r'^\d\d-domain-(\d)-questions.md',r'domain-\1-answer-key.md',name)
            key_path = str(Path(path).parent / 'answer-keys' / key_name).replace('\\','/')
            key = dict(re.findall(r'^(\d+)-([A-D])\s*$',texts.get(key_path,''),re.M))
            if key.get(str(row['reviewed_question_number'])) != row['reviewed_answer']:
                failures.append(f'{qid}: external key mismatch')
            if len(key) != len(re.findall(r'^## Question \d+',texts[path],re.M)):
                failures.append(f'{key_path}: orphan or missing key entries')
    for path,numbers in numbered.items():
        if sorted(numbers) != list(range(1,len(numbers)+1)):
            failures.append(f'{path}: nonsequential question numbers')
    return failures

def language_failures(files: list[Path]) -> list[str]:
    # Phrase-aware checks target semantic false friends as well as Portuguese.
    # Human editorial review remains necessary; this is not proof of technical truth.
    portuguese = re.compile(r'\b(?:questões?|gabaritos?|respostas?|segurança|conformidade|revisão|acompanhe|simulados?|computação|armazenamento|permissões|gratuito|introdução|estamos construindo|dica de prova|menor privilégio|nuvem|domínio)\b',re.I)
    bad_english = re.compile(r'\b(?:proof signals?|mental rule of proof|in-memory banks|scratch surface|without compromise|Café Overview|cloud payloads)\b',re.I)
    failures = []
    for p in files:
        relative = p.relative_to(ROOT).as_posix()
        if relative.startswith('docs/english-edition/'):
            continue
        raw = p.read_text(encoding='utf-8-sig')
        if relative == 'assets/README.md':
            raw = raw.split('## Original banner language')[0]
        raw = re.sub(r'https?://[^\s<>\)\"]+', '', raw)
        raw = re.sub(r'<(?:style|script)\b[^>]*>.*?</(?:style|script)>', '', raw, flags=re.S)
        for number,line in enumerate(raw.splitlines(),1):
            if portuguese.search(line) or bad_english.search(line) or re.search(r'ZXQ\w+ZXQ|PT-BR|Domain [15] to 5|Domain 5|waitlist|early access',line,re.I):
                failures.append(f'{relative}:{number}: {line.strip()}')
    return failures

def validate() -> dict[str,Any]:
    inventory = read_json(AUDIT / 'source-inventory.json')
    audit = read_json(AUDIT / 'question-audit.json')
    files = content_files()
    texts = {p.relative_to(ROOT).as_posix():p.read_text(encoding='utf-8-sig') for p in files}
    coverage = []
    for row in inventory['files']:
        p = ROOT / row['target_path']
        if not p.is_file():
            coverage.append(f'missing original equivalent: {row["target_path"]}')
            continue
        if row['reviewed_english_hash'] and sha256(p) != row['reviewed_english_hash']:
            coverage.append(f'reviewed hash differs: {row["target_path"]}')
        if row['translation_classification'].startswith('preserve') and sha256(p) != row['original_hash']:
            coverage.append(f'original asset/license changed: {row["target_path"]}')
        if p.suffix == '.md':
            before = len(row['educational_structure']['headings'])
            after = len(re.findall(r'^#{1,6}\s+',texts[row['target_path']],re.M))
            if after < before:
                coverage.append(f'fewer sections than the source: {row["target_path"]} ({before}->{after})')
    modules = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and re.match(r'^\d\d-',p.name))
    if [int(p[:2]) for p in modules] != list(range(1,19)):
        coverage.append('18 numbered modules not preserved')
    if inventory['file_count'] != 180 or inventory['markdown_count'] != 172:
        coverage.append('source baseline differs from verified checkout')
    questions = question_failures(texts,audit)
    coverage.extend(source_integrity(inventory, audit))
    coverage.extend(obsolete_path_failures(files, inventory))
    if len(audit['questions']) != 96 or audit['multiple_choice_count'] != 44:
        questions.append('full source prompt coverage differs from 96/44')
    html = BeautifulSoup(texts['index.html'],'html.parser')
    portal = []
    if html.html.get('lang') != 'en-US' or len(html.select('a.mod-link')) != 18:
        portal.append('portal language/module links differ')
    if len(re.findall(r'^## Question \d+',texts['16-Practice-Exams-and-Questions/10-question-practice-exam.md'],re.M)) != 10:
        questions.append('short practice exam does not contain ten questions')
    checks = {'source_coverage':coverage,'question_integrity':questions,'navigation':link_failures(files),'language_regressions':language_failures(files),'markdown_structure':markdown_failures(files),'portal_structure':portal}
    return {'status':'passed' if not any(checks.values()) else 'failed','source_commit':inventory['source_commit'],'original_files':180,'original_markdown_documents':172,'modules':len(modules),'reviewed_prompts':96,'multiple_choice_questions':44,'open_response_prompts':52,'checks':{key:{'status':'passed' if not value else 'failed','failures':value} for key,value in checks.items()},'limitations':['Language regression rules complement manual semantic editing; they do not certify technical accuracy.','AWS labs were statically reviewed, not executed.','Browser and published-file checks are recorded separately.']}

if __name__ == '__main__':
    result = validate()
    (AUDIT/'validation-results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,ensure_ascii=False))
    sys.exit(0 if result['status']=='passed' else 1)
