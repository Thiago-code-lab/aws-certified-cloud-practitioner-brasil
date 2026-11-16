# English edition audit

## Publication checkpoint — November 16, 2026

The final publication pass began with `git fetch origin`, `git switch clf-c02-english`, `git status`, and `git log -5 --oneline`. The working tree was clean, and both local `HEAD` and `origin/clf-c02-english` were already at the published audit commit `9d6a09932a8137d672af0dd10b2b116034e60bce`. All prior corrections were retained.

Re-ran all four required commands in this pass: dependency installation succeeded, the complete offline validator passed, **all 19 unit tests passed**, and `git diff --check` passed. The validator reconfirmed 180 mapped source files, 172 Markdown documents, 18 modules, 96 unique exercise prompts, preserved inline answer letters, matching current external keys, and the 21 documented historical discrepancies. No further educational corrections or answer changes were required. This follow-up changes only this audit report; the cumulative final review still changes 90 distinct files relative to `6dc4989bee92978c2bf4d0610cf0ca7a425efc2b`.

Compared all 172 mapped Markdown files with their Portuguese source for coverage, heading preservation, word-count contraction, and bullet-count reductions. The size/count screen flagged only the three labs because their original verification bullets became explicit prose and numbered procedures. Manual comparison of those source labs confirmed that their identity/access, static-hosting, monitoring, verification, and cleanup objectives remain represented in the expanded English instructions. Also compared representative cloud-computing, shared-responsibility, and support lessons directly with their Portuguese originals. These screens support content-preservation review; counts alone do not establish semantic equivalence. The earlier manual English review and SAA style comparison documented below remain applicable.

Reopened the [official CLF-C02 guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) and [current AWS Support comparison](https://aws.amazon.com/premiumsupport/plans/); their domain and support-plan descriptions remain consistent with the reviewed edition. The previous external-link check remains recorded separately rather than being presented as a new network check. AWS labs and browser checks were not executed in this follow-up.

Local and remote `main` remained at `a59548c0d73c9da1cb20e7314cf46f983088e97a`. No remote `gh-pages` branch was advertised at the start of this pass; none was created or modified. Publication is limited to `origin/clf-c02-english`, without force-push, pull requests, or deployment changes.

The final publication procedure is to commit this checkpoint, push `clf-c02-english`, fetch again, and compare `git rev-parse HEAD`, `git rev-parse origin/clf-c02-english`, and `git ls-remote origin refs/heads/clf-c02-english`, with a clean `git status`. The checkpoint commit's immutable SHA is available in the [English branch commit history](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil/commits/clf-c02-english/) and the completion report. A commit cannot embed its own SHA without changing that SHA.

## Final quality review — November 16, 2026

Reviewed from baseline `6dc4989bee92978c2bf4d0610cf0ca7a425efc2b`, exclusively on `clf-c02-english`. All 18 modules and 96 exercises remain present. This pass changes 90 files: 83 learning Markdown documents, two validator/test files, three existing audit JSON files, one new external-link results file, and this report. Unmodified documents were reviewed as well.

### Manual editorial and technical review

- Read the substantive English text of all **172 source-mapped Markdown documents**, including 44 multiple-choice questions and 52 open-response prompts. Shared CloudStudy footer text was reviewed once. This was an English editorial review, not a repeated line-by-line translation comparison of every Portuguese original. The [editorial manifest](editorial-manifest.json) records the method and result for each document.
- Corrected literal translations such as “most charged network services,” “ECS/EKS orchestra,” and “Orchestral pipeline”; repaired sentence fragments, grammar, service capitalization, root-user terminology, and inconsistent review headings. Preserved explanations and learning objectives rather than shortening lessons.
- Distinguished EC2 Savings Plans spend commitments, Reserved Instance configuration commitments, Regional versus zonal reservations, and On-Demand Capacity Reservations. Clarified that immediate-use capacity reservations have no term commitment while future-dated reservations can require one. See the [EC2 purchasing lesson](../../02-Amazon-EC2/02-pricing-models.md) and its official references.
- Expanded [S3 storage-class distinctions](../../04-Amazon-S3/02-storage-classes.md): Instant Retrieval versus asynchronous Glacier retrieval, single-AZ resilience, minimum storage durations, retrieval charges, and Intelligent-Tiering monitoring and optional archive tiers.
- Corrected public/private subnet definitions and explained stateful security-group allow rules versus stateless network ACL allow/deny rules, including return traffic. Clarified Step Functions retries, DMS database engines, EFS grammar, CloudFront caching, and SageMaker AI naming.
- Rechecked IAM, shared responsibility, Regions/AZs, the six CAF perspectives, the six Well-Architected pillars, AI service purposes, current Support offerings, Free Tier eligibility, and official CLF-C02 domains against selected primary AWS sources. Added the Enterprise On-Ramp transition context to the support lesson. Retained the existing lifecycle caveats for Snow Family, Migration Hub, Mainframe Modernization, CodeCommit, and X-Ray after checking their official notices. The manifest lists the primary sources checked in this pass.
- Compared the SAA English branch's README and EC2 module with this edition. Applied useful consistency in GitHub navigation, English service names, scenario-based writing, and pricing-versus-capacity explanations while retaining this curriculum's beginner level and CloudStudy branding.

### Practice-question findings

All **96 prompts** received manual content review. The 44 multiple-choice questions retain their correct answer letters; no answer-letter change was required. Reviewed the alternatives and explanations for a single defensible answer, and checked domain metadata against the four official domains. The Region-definition question retains domain 3 metadata within its original domain 1 study set. The 52 open-response answers remain intact apart from justified wording improvements.

Revalidated all **21 historical external-key discrepancies** against the Portuguese source keys and inline answers. Each now has a question-specific technical justification in [question-audit.json](question-audit.json), explaining both the retained answer and the rejected historical letter, with an official reference. The validator checks historical external letters against Git source content and rejects missing discrepancy justifications. Existing orphaned historical answer entries remain recorded as evidence; no exercises were deleted.

These questions are learning aids, not official AWS questions or a full-length, domain-weighted exam simulation.

### Automated validation and navigation

The final local checks completed successfully:

| Check executed | Result |
|---|---|
| `python -m pip install -r scripts/english-edition/requirements.txt` | Passed; pinned requirements already installed. Pip reported unrelated pre-existing invalid-distribution warnings in the host environment. |
| `python scripts/english-edition/validate.py` | Passed: 180 source equivalents, 172 original Markdown documents, 18 modules, 96 question IDs, original inline answers and historical keys, current answer keys, local links/images/anchors, language regression rules, and Markdown structure. |
| `python -m unittest discover -s scripts/english-edition -p "test_*.py"` | **19 tests passed**, including the original seven tests and 12 added regression/mutation cases. |
| `git diff --check` and staged diff check | Passed. |
| Exact-content duplicate scan of the 172 source-mapped Markdown documents, normalizing line endings | No duplicates. Source coverage found no omitted materials; no files were deleted. |
| External URL reachability, including bare URLs and image references in learning Markdown | **141 unique URLs checked: 137 returned HTTP 200; four LinkedIn URLs returned HTTP 999 and remain unverified.** |

The strengthened Markdown checks reject missing/extra table cells, missing or empty expandable-answer summaries, and malformed bare closing link syntax. Heading anchors are derived from parsed Markdown, including Setext headings, so code comments inside fences do not create false heading targets. These targeted checks are not a complete Markdown lint specification.

Fixed the malformed Free Tier link; added direct links to labs and cheatsheets; corrected module transitions; linked the glossary/resources back to the module table; and added a compact README navigation bar and useful official study links. Clarified that review topics such as storage are not additional official exam domains. Local documentation navigation has no detected missing files, images, or heading anchors. Existing external URLs were checked against the starting English tree: none were removed.

See [offline validation results](validation-results.json) and [external-link results](external-link-results.json). HTTP reachability does not establish the correctness of a remote page or verify its fragment anchors.

### Limitations and publication safety

- **AWS labs were not executed** and no AWS resources were provisioned. Lab steps, access assumptions, costs, verification, and cleanup received static review only.
- Four preserved LinkedIn attribution/branding URLs blocked automated verification with HTTP 999. Their destination availability remains unverified; they are not classified as confirmed broken links. Other external services and AWS documentation can change after review.
- Original Portuguese banner artwork is preserved with the English caption. Promotional destinations can contain Portuguese. Language checks and manual review cannot prove complete semantic equivalence or absence of every editorial defect.
- No browser validation was rerun. Inherited browser artifacts are historical evidence only. The HTML portal, frontend/deployment infrastructure, licensing, raster assets, and branding were not changed in this pass. No pull request was opened or merged.
- Both local `main` and remote `origin/main` were verified at `a59548c0d73c9da1cb20e7314cf46f983088e97a`, unchanged from the start. Only `clf-c02-english` is the push target.

### Final commits

- Corrections, refreshed inventories, external-link evidence, and expanded validator/tests: `696397c61f1ffc0ab4ee357439276bedc7aa0eb4` (`docs(en): polish technical writing and verify final study materials`).
- Original final audit report: `9d6a09932a8137d672af0dd10b2b116034e60bce` (`test(en): record final documentation quality audit`).
- Publication checkpoint: the subsequent commit titled `docs(en): finalize CLF-C02 English edition quality review`. Resolve its exact hash with `git log -1 --format=%H -- docs/english-edition/README.md` or the [English branch commit history](https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil/commits/clf-c02-english/).

The earlier edition inventory and translation audit follow below for traceability.

---

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
