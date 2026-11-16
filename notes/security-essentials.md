# Essential Security - Exam Review

## Quick review
- IAM controls identities, permissions and roles.
- MFA reduces the risk from compromised credentials, but does not replace least privilege.
- CloudTrail logs API calls for auditing.

## Common exam clue
If it says "trace API calls", the normal association is CloudTrail.

## Common error
Assuming that AWS sets account permissions for the customer.

## What to memorize
| Comparison | Mental rule |
|---|---|
| IAM User vs Role | User is persistent; Role is a persistent identity assumed using temporary credentials |
| MFA vs IAM policy | MFA authenticates better; policy authorizes or denies |

<!-- question-id: CLF-NOTE-002; domain: 2; type: open-response -->
## Validation question
An application needs to access another AWS service without storing permanent keys. Which IAM feature should come to mind?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
IAM Role with least-privilege permissions for the task.


[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
