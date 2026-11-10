# S3 Essential - Test Review

## Quick Review
- S3 is object storage, not block volume.
- Versioning helps against accidental deletion or overwriting.
- Lifecycle optimizes cost with transition and automatic expiration.

## Classic proof signal
If the statement talks about long-term archiving with rare access, the clue is usually Glacier.

## Common error
Use S3 as if it were an EC2 operating system disk.

## What to memorize
| Comparison | Mental rule |
|---|---|
| S3 Standard vs Glacier | Standard for frequent use; Glacier for archive |
| Versioning vs Lifecycle | Recover versions vs automate lifecycle |

## Validation question
A bucket receives monthly reports and must move old files to cheaper storage without manual action. Which resource to use?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Lifecycle.

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
