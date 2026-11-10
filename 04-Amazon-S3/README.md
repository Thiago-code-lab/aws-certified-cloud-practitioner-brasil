#Amazon S3

Object storage module focusing on durability, classes and cost.

## Module focus
- Objects, buckets and access policies.
- Versioning and lifecycle.
- Typical storage classes and scenarios.

## Quick Review
- S3 is an object, not a block for EC2 boot.
- Versioning reduces the risk of accidental deletion.
- Lifecycle moves data to cheaper class according to access pattern.

## Classic proof signals
- "Simple static website" -> S3 static website hosting.
- "Data rarely accessed for years" -> Glacier/Deep Archive.
- "Access control at scale" -> IAM policy + bucket policy.

## Common error
Choose class only for lowest price per GB and ignore cost/recovery time.

## What to memorize
| Comparison | Mental rule of proof |
|---|---|
| S3 Standard vs S3 Glacier | Standard for frequent access; Glacier for archive and rare access |
| Versioning vs Lifecycle | Versioning protects history; Lifecycle optimizes cost over time |

## Bridge to next module
After S3, move on to costs: how to price usage, predict spending and avoid surprises.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil


> If the objective is also data engineering, this course helps you transform the AWS base into projects: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
