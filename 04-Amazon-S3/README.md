# Amazon S3

Object storage module focusing on durability, classes and cost.

## Module focus
- Objects, buckets and access policies.
- Versioning and lifecycle.
- Typical storage classes and scenarios.

## Quick review
- S3 stores objects; it does not provide an EC2 boot volume.
- Versioning reduces the risk of accidental deletion.
- Lifecycle rules transition objects to appropriate storage classes or expire them over time.

## Common exam clues
- "Simple static website" -> S3 static website hosting.
- "Data rarely accessed for years" -> Glacier/Deep Archive.
- "Access control at scale" -> IAM policy + bucket policy.

## Common error
Choosing a class only for the lowest price per GB and ignoring retrieval costs and retrieval time.

## What to memorize
| Comparison | Exam rule of thumb |
|---|---|
| S3 Standard vs S3 Glacier | Standard for frequent access; Glacier for archive and rare access |
| Versioning vs Lifecycle | Versioning protects history; Lifecycle optimizes cost over time |

## Bridge to next module
After S3, move on to [networking](../05-Networking-and-Connectivity/README.md): subnets, routing, and connectivity.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


> If the objective is also data engineering, this course helps you transform the AWS fundamentals into projects: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [AWS reference 2](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Lessons and practice

- [Basic Concepts](01-basic-concepts.md)
- [Storage Classes](02-storage-classes.md)
- [Policies and ACLs](03-policies-and-acls.md)
- [Versioning and Lifecycle](04-versioning-and-lifecycle.md)
- [S3 Transfer Acceleration](05-s3-transfer-acceleration.md)
- [Static Website](06-static-website.md)

[Back to all modules](../README.md#modules)
