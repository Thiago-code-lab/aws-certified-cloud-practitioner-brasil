# Storage

Module for comparing storage types without delving beyond the CLF-C02 level.

## Module focus
- S3 for objects.
- EBS for block.
- EFS for shared file.

## Quick Review
- Object is accessed via API and combines data + metadata.
- Block is used as volume by instances.
- Shared file serves multiple clients with file system.

## Common exam clues
- "Store objects, images, backups or logs" -> Amazon S3.
- "Persistent disk for EC2" -> Amazon EBS.
- "File system shared between Linux instances" -> Amazon EFS.

## Common error
Use S3 as a response for any storage. The exam distinguishes object, block and file.

## What to memorize
| Comparison | Exam rule of thumb |
|---|---|
| S3 vs EBS | S3 = objects; EBS = block for EC2 |
| EBS vs EFS | EBS = individual volume; EFS = shared file |

## Bridge to next module
With storage understood, move on to monitoring and governance: how to observe, audit, and control the environment.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english

---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Lessons and practice

- [EBS](01-ebs.md)
- [EFS](02-efs.md)
- [FSx](03-fsx.md)
- [AWS Storage Gateway](04-aws-storage-gateway.md)
- [AWS Snow Family](05-aws-snow-family.md)
- [AWS Backup](06-aws-backup.md)

[Back to all modules](../README.md#modules)
