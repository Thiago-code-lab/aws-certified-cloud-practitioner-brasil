# Domain Review - IAM and Security

Use this block when errors involve access, auditing, encryption, or customer responsibility.

## Quick review
- Root should be protected with MFA and avoided in daily use.
- IAM User is persistent identity; IAM roles are persistent identities assumed for temporary sessions.
- CloudTrail logs API calls for auditing.
- KMS centralizes managed encryption keys.

## Common exam clues
- If it says "who did what in the account", think CloudTrail.
- If it says "temporary access between services", think IAM Role.
- If you see "AWS compliance reports", think AWS Artifact.

## What to memorize
| Comparison | Mental rule |
|---|---|
| IAM User vs Role | User = long term; Role = assumed access |
| MFA vs IAM policy | MFA strengthens authentication; policy authorizes |
| CloudTrail vs CloudWatch | API audit vs operational metrics/logs |

## Next review
After this block, proceed to [storage](./storage.md): permissions and data appear together in many questions.

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
