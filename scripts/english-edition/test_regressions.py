"""Mutation tests using the actual reviewed corpus, without modifying files."""
from __future__ import annotations
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from validate import AUDIT, ROOT, anchors, markdown_failures, question_failures, read_json, source_integrity, table_failures


class MarkdownRegressionTests(unittest.TestCase):
    def test_missing_table_cell_is_rejected(self) -> None:
        self.assertTrue(table_failures('| A | B |\n|---|---|\n| one |\n', 'table.md'))

    def test_extra_table_cell_is_rejected(self) -> None:
        self.assertTrue(table_failures('| A | B |\n|---|---|\n| one | two | three |\n', 'table.md'))

    def test_escaped_pipe_is_one_cell(self) -> None:
        self.assertEqual([], table_failures('| A | B |\n|---|---|\n| one \\| two | three |\n', 'table.md'))

    def check_markdown(self, text: str) -> list[str]:
        with TemporaryDirectory(dir=ROOT) as directory:
            path = Path(directory) / 'sample.md'
            path.write_text(text, encoding='utf-8')
            return markdown_failures([path])

    def test_expandable_answer_requires_summary(self) -> None:
        self.assertTrue(self.check_markdown('<details>\nAnswer\n</details>\n'))

    def test_valid_expandable_answer(self) -> None:
        self.assertEqual([], self.check_markdown('<details>\n<summary>Answer</summary>\n\nText\n</details>\n'))

    def test_empty_summary_is_rejected(self) -> None:
        self.assertTrue(self.check_markdown('<details>\n<summary></summary>\nAnswer\n</details>\n'))

    def test_unclosed_code_fence_is_rejected(self) -> None:
        self.assertTrue(self.check_markdown('```sh\necho example\n'))

    def test_valid_inline_link(self) -> None:
        self.assertEqual([], self.check_markdown('Check [AWS Free Tier](https://aws.amazon.com/free/).\n'))

    def test_malformed_inline_link_is_rejected(self) -> None:
        self.assertTrue(self.check_markdown('Check AWS Free Tier](https://aws.amazon.com/free/).\n'))

    def test_code_fence_does_not_create_heading_anchor(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.md'
            path.write_text('# Real\n\n```sh\n# Fake\n```\n\nSetext\n------\n', encoding='utf-8')
            self.assertEqual({'real', 'setext'}, anchors(path))

class QuestionMutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = read_json(AUDIT/'question-audit.json')
        cls.texts = {p.relative_to(ROOT).as_posix():p.read_text(encoding='utf-8') for p in ROOT.rglob('*.md') if '.git' not in p.parts}

    def test_reviewed_corpus(self) -> None:
        self.assertEqual([],question_failures(self.texts,self.audit))

    def test_source_answers_are_preserved(self) -> None:
        inventory = read_json(AUDIT / 'source-inventory.json')
        self.assertEqual([], source_integrity(inventory, self.audit))

    def test_consistently_changed_answer_still_fails_source_check(self) -> None:
        from copy import deepcopy
        audit = deepcopy(self.audit)
        audit['questions'][0]['reviewed_answer'] = 'A'
        failures = source_integrity(read_json(AUDIT / 'source-inventory.json'), audit)
        self.assertTrue(any('original correct inline answer changed' in f for f in failures))

    def test_historical_key_tampering_is_rejected(self) -> None:
        from copy import deepcopy
        audit = deepcopy(self.audit)
        audit['questions'][0]['original_answer']['external'] = 'D'
        failures = source_integrity(read_json(AUDIT / 'source-inventory.json'), audit)
        self.assertTrue(any('historical external key differs' in f for f in failures))

    def test_discrepancy_without_justification_is_rejected(self) -> None:
        from copy import deepcopy
        audit = deepcopy(self.audit)
        audit['questions'][0].pop('final_review_justification', None)
        failures = source_integrity(read_json(AUDIT / 'source-inventory.json'), audit)
        self.assertTrue(any('missing technical justification' in f for f in failures))

    def test_external_mismatch_is_rejected(self) -> None:
        texts = self.texts.copy()
        key = '16-Practice-Exams-and-Questions/answer-keys/practice-exam-answer-key.md'
        texts[key] = texts[key].replace('2-A','2-B',1)
        self.assertTrue(any('external key mismatch' in f for f in question_failures(texts,self.audit)))

    def test_inline_mismatch_is_rejected(self) -> None:
        texts = self.texts.copy()
        key = '16-Practice-Exams-and-Questions/10-question-practice-exam.md'
        texts[key] = texts[key].replace('**Correct answer:** B','**Correct answer:** A',1)
        self.assertTrue(any('inline answer differs' in f for f in question_failures(texts,self.audit)))

    def test_missing_option_is_rejected(self) -> None:
        texts = self.texts.copy()
        key = '16-Practice-Exams-and-Questions/10-question-practice-exam.md'
        texts[key] = texts[key].replace('D) Fixed latency','',1)
        self.assertTrue(any('four distinct options' in f for f in question_failures(texts,self.audit)))

    def test_missing_rationale_is_rejected(self) -> None:
        texts = self.texts.copy()
        key = '16-Practice-Exams-and-Questions/10-question-practice-exam.md'
        texts[key] = texts[key].replace('**D — Incorrect:**','**D:**',1)
        self.assertTrue(any('rationale' in f for f in question_failures(texts,self.audit)))

if __name__ == '__main__':
    unittest.main()
