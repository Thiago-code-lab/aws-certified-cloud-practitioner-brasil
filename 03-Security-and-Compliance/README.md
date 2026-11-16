# Security and Compliance

Module focused on what is most tested: identity, access, auditing and responsibility.

## Module focus
- IAM: users, groups, roles and policies.
- MFA and least privilege.
- Audit with CloudTrail and compliance base.

## Quick Review
- Root must be restricted and protected with MFA.
- IAM controls authentication and authorization.
- CloudTrail responds to "who did what" via API events.

## Common exam clues
- "Trace API calls" -> CloudTrail.
- "Grant temporary access between services" -> IAM Role.
- "Enforce minimum required access" -> principle of least privilege.

## Common error
Assuming that enabling IAM alone establishes compliance. The exam covers a combination of controls, including logging and governance.

## What to memorize
| Comparison | Exam rule of thumb |
|---|---|
| IAM User vs IAM Role | User = long-term identity; Role = assumed permission, including temporary |
| Root vs IAM Admin | Root for exceptional tasks; federated roles for routine operation |

## Bridge to next module
With access and controls defined, the natural next step is to review storage, especially S3.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


> To study practical data applications after this topic, this Data Engineering course on AWS complements it well: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS reference 2](https://aws.amazon.com/compliance/shared-responsibility-model/)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Lessons and practice

- [Shared Responsibility Model](01-shared-responsibility-model.md)
- [IAM](02-iam.md)
- [AWS Organizations](03-aws-organizations.md)
- [AWS Shield and WAF](04-aws-shield-and-waf.md)
- [Amazon Inspector and GuardDuty](05-amazon-inspector-and-guardduty.md)
- [AWS KMS and Secrets Manager](06-aws-kms-and-secrets-manager.md)
- [AWS Config](07-aws-config.md)
- [AWS CloudTrail](08-aws-cloudtrail.md)
- [AWS Artifact](09-aws-artifact.md)
- [Compliance Programs](10-compliance-programs.md)

[Back to all modules](../README.md#modules)
