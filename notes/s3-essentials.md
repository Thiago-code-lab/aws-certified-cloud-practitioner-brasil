# S3 Essentials - Exam Review

## Quick review
- S3 is object storage, not block volume.
- Versioning helps against accidental deletion or overwriting.
- Lifecycle optimizes cost with transition and automatic expiration.

## Common exam clue
If the statement talks about long-term archiving with rare access, the clue is usually Glacier.

## Common error
Using S3 as if it were an EC2 operating system disk.

## What to memorize
| Comparison | Mental rule |
|---|---|
| S3 Standard vs Glacier | Standard for frequent use; Glacier for archive |
| Versioning vs Lifecycle | Recover versions vs automate lifecycle |

<!-- question-id: CLF-NOTE-003; domain: 3; type: open-response -->
## Validation question
A bucket receives monthly reports and must move old files to cheaper storage without manual action. Which feature should it use?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Lifecycle.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
