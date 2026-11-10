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

## Classic proof signals
- "Trace API calls" -> CloudTrail.
- "Grant temporary access between services" -> IAM Role.
- "Enforce minimum required access" -> principle of least privilege.

## Common error
Think that enabling IAM alone resolves compliance. Prova charges a set of controls, including logging and governance.

## What to memorize
| Comparison | Mental rule of proof |
|---|---|
| IAM User vs IAM Role | User = long-term identity; Role = assumed permission, including temporary |
| Root vs IAM Admin | Root for exceptional tasks; IAM Admin for daily operation |

## Bridge to next module
With access and controls defined, the natural next step is to review storage, especially S3.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil


> To study practical data applications after this topic, this Data Engineering course on AWS complements it well: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
