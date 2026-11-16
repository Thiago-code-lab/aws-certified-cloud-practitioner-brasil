# Key Services

Compact map for reviewing service associations for the exam without turning the review into a complete catalog.

## Fundamentals
- Region: geographic location, latency and data residency.
- AZ: local isolation for high availability.
- Shared responsibility: AWS protects infrastructure; customer protects data, access and configurations.
- Exam clue: if the statement talks about local physical isolation, it normally points to AZ.

## IAM and security
- IAM: identity, authentication and authorization.
- CloudTrail: API call audit trail.
- KMS: encryption keys.
- Artifact: compliance documents and reports.
- Exam clue: if it says "who did what in the account", the most common association is CloudTrail.

## S3 and storage
- S3: Object storage.
- EBS: block volume for EC2.
- EFS: Shared file system.
- Lifecycle: cost reduction over time.
- Exam clue: if you talk about data rarely accessed for years, think Glacier.

## Costs and pricing
- Budgets: limit alert.
- Cost Explorer: historical and trend analysis.
- Pricing Calculator: estimate before use.
- Spot: low cost with interruption.
- Exam clue: if the workload tolerates interruption, Spot is usually the best clue.

## Quick Comparisons
| Comparison | Exam use |
|---|---|
| Region vs AZ | Region = geography; AZ = isolation for availability |
| IAM User vs Role | User = persistent identity; Role = assumed identity with temporary credentials |
| CloudWatch vs CloudTrail | CloudWatch observes operation; CloudTrail audits API |
| S3 vs EBS | S3 = objects; EBS = block for instance |
| S3 Standard vs Glacier | Standard = frequent access; Glacier = archive |
| On-Demand vs Spot | On-Demand = flexibility; Spot = savings with interruption |
| Budgets vs Cost Explorer | Budgets = alert; Cost Explorer = analysis |

## Final tip
When two alternatives seem correct, choose the one that solves the scenario with less operational complexity and better alignment with the statement.

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
