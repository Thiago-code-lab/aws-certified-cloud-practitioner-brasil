"""Mutation tests using the actual reviewed corpus, without modifying files."""
from __future__ import annotations
import unittest
from validate import AUDIT, ROOT, question_failures, read_json, source_integrity

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
