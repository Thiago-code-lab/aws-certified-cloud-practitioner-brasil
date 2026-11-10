# Essential Safety - Proof Review

## Quick Review
- IAM controls identities, permissions and roles.
- MFA reduces risk of compromised credential, but does not replace lesser privilege.
- CloudTrail logs API calls for auditing.

## Classic proof signal
If it says "trace API calls", the normal association is CloudTrail.

## Common error
Assume that AWS sets account permissions for the customer.

## What to memorize
| Comparison | Mental rule |
|---|---|
| IAM User vs Role | User is persistent; Role is temporary/assumed |
| MFA vs IAM policy | MFA authenticates better; policy authorizes or denies |

## Validation question
An application needs to access another AWS service without storing permanent keys. Which IAM feature should come to mind?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
IAM Role with minimum permissions for the task.

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
