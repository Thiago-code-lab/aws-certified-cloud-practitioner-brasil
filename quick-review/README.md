# Quick Review - CLF-C02

Use this block for 20-30 minute sessions, focused by study topic. It doesn't replace flashcards: here the idea is to quickly diagnose gaps before returning to the right module.

## Review by topic
| Study topic | Short review | When to use |
|---|---|---|
| Cloud Fundamentals | [fundamentals.md](./fundamentals.md) | When you confuse Regions, AZs, elasticity, or shared responsibility |
| IAM and security | [security.md](./security.md) | When you get identity, permissions, auditing or compliance wrong |
| S3 and Storage | [storage.md](./storage.md) | When you confuse S3, EBS, EFS, storage classes, or lifecycle rules |
| Costs and pricing | [costs.md](./costs.md) | When you struggle with Budgets, Cost Explorer, Spot, support, or pricing models |

Storage is part of official domain 3, Cloud Technology and Services. These topic groupings are review aids, not additional exam domains.

## Suggested flow
1. Run the [exam-eve checklist](./exam-eve-checklist.md).
2. Review the domain with the most errors using the files above.
3. See [key services](./key-services.md) for quick comparison.
4. Reread [common errors](./common-mistakes.md) before solving new questions.

## Mini diagnostic training

<!-- question-id: CLF-QUICK-001; domain: 1; select: 1 -->
### Question 1
An application must remain available if an isolated data center in the Region fails. Which design best addresses this availability requirement?

A) Multi-AZ

B) Root user with MFA

C) S3 Glacier Deep Archive

D) AWS Budgets

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

- **A — Correct:** A multi-zone application with failover reduces localized failure impact.

- **B — Incorrect:** Root MFA improves account authentication, not application redundancy.

- **C — Incorrect:** Glacier Deep Archive provides archive storage, not application failover.

- **D — Incorrect:** Budgets notifies on spending thresholds, not service failures.

[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

<!-- question-id: CLF-QUICK-002; domain: 2; select: 1 -->
### Question 2
A team wants to allow an EC2 application to access an S3 bucket without storing access keys on the server. Which option is most suitable?

A) IAM role for the EC2 instance

B) AWS Artifact

C) Business Support+

D) S3 Lifecycle

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

- **A — Correct:** An instance profile supplies temporary credentials from an IAM role with the required S3 permissions.

- **B — Incorrect:** Artifact provides compliance reports, not workload credentials.

- **C — Incorrect:** A support plan does not provide an application's S3 authorization.

- **D — Incorrect:** Lifecycle manages object transitions and expiration, not identity.

[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

<!-- question-id: CLF-QUICK-003; domain: 3; select: 1 -->
### Question 3
Log files must be kept for years, almost never accessed, and can take hours to retrieve. Which choice best fits these requirements?

A) S3 Glacier Deep Archive

B) S3 Standard

C) EBS gp3

D) EC2 On-Demand

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

- **A — Correct:** Deep Archive fits very infrequent access when retrieval delays of hours are acceptable; minimum storage duration and retrieval fees still apply.

- **B — Incorrect:** Standard supports frequent low-latency access at a higher storage price.

- **C — Incorrect:** EBS gp3 is block storage for EC2, not a low-cost long-term object archive.

- **D — Incorrect:** EC2 On-Demand purchases compute rather than archival object storage.

[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-QUICK-004; domain: 4; select: 1 -->
### Question 4
Before launching an architecture, the company wants to estimate its monthly cost. Which tool should it use?

A) AWS Pricing Calculator

B) AWS CloudTrail

C) Amazon GuardDuty

D) S3 Transfer Acceleration

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

- **A — Correct:** Pricing Calculator estimates planned usage and configuration costs.

- **B — Incorrect:** CloudTrail records supported account actions.

- **C — Incorrect:** GuardDuty detects threats.

- **D — Incorrect:** Transfer Acceleration optimizes certain S3 transfer routes and does not estimate architecture costs.

[AWS reference](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html)

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
