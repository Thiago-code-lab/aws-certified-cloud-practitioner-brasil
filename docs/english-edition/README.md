# English edition audit

This edition translates all 172 Markdown documents in the Portuguese source at commit `a59548c0d73c9da1cb20e7314cf46f983088e97a`. It retains all 18 numbered modules, the original practice exercises, flashcards, notes, cheatsheets, labs, glossary, contribution documents, and project assets.

The organization follows the [SAA-C03 English edition](https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english): descriptive English paths, GitHub-native module navigation, preserved CloudStudy branding, and links to official AWS references. The existing published Cloud Computing and EC2 filenames are retained.

## Coverage and naming

- [Source inventory](source-inventory.json): one source-to-target mapping for each of the 180 original files, including 172 Markdown documents, two SVG diagrams, four PNG images, the license, and the existing HTML file.
- 148 file paths differ from Portuguese `main`; 79 basenames and 15 directory paths are translated. Directory counts include the nested answer-key directory.
- The human-readable text in both SVG diagrams is English. Original raster artwork and the MIT license are preserved byte for byte. The Portuguese banner remains original artwork; its English caption appears in the main README.
- [Editorial manifest](editorial-manifest.json): document references and review scope.

## Practice questions and answer preservation

The [question audit](question-audit.json) maps all 96 source prompts: 44 multiple-choice questions and 52 open-response prompts. Module 16 contains 40 multiple-choice questions; Quick Review contains four. The short practice exam contains ten questions.

Original question order, alternatives, numbering, and correct inline answer letters are preserved. The Region-definition question remains in its original domain 1 study set; its metadata identifies official domain 3 for review.

The Portuguese source has 21 disagreements between external answer keys and correct answers stated in the questions. English external keys follow the original inline answers and explanations. Each discrepancy, original key letter, and retained correct letter is recorded in the question audit. These corrections reconcile contradictory answer sheets without changing a question's correct answer.

Some source labels treated supplementary cross-domain practice as a fifth exam domain. This edition labels it as cross-domain review: CLF-C02 has four official domains. The original six exercises remain available.

## Validation

From the repository root, install the offline validator dependencies and run:

```sh
python -m pip install -r scripts/english-edition/requirements.txt
python scripts/english-edition/validate.py
python -m unittest discover -s scripts/english-edition -p "test_*.py"
git diff --check
```

[Validation results](validation-results.json) cover source-tree equivalence, all 18 modules, original inline answers, question and external-key consistency, relative links and image references, heading anchors, expandable answers, code fences, and targeted language regressions. Mutation tests confirm that wrong answers, missing alternatives, and missing explanations are rejected.

## Technical references and limitations

The [official CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html), [revision history](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-revisions.html), and [AWS Support comparison](https://aws.amazon.com/premiumsupport/plans/) were checked on November 16, 2026. The guide revision history lists version 1.3, published October 29, 2026. Lessons retain source topics and distinguish historical services from current availability where relevant.

Language checks detect common regressions and complement editorial reading; they cannot prove semantic equivalence. AWS labs received static review and were not executed against an AWS account. Promotional URLs and original branding are preserved; external services can change independently.

The HTML localization, browser-check script, screenshots, and browser results already present in the working directory were inherited. They are supplementary artifacts, not evidence of a new browser run for this finalization. No GitHub Pages configuration, deployment workflow, frontend application, or hosting dependency was added.

[Return to the learning path](../../README.md)
