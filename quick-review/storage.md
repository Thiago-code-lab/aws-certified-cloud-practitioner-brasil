# Domain Review - S3 and Storage

Use this block when errors involve S3, storage classes, backup, or volume type.

## Quick Review
- S3 stores objects in buckets.
- EBS is persistent block for EC2.
- EFS is shared file system.
- Lifecycle automatically moves or expires objects to control cost.

## Common exam clues
- If it says "object, backup, log, or static site", think S3.
- If it says "disk for EC2 instance", think EBS.
- If it says "file shared by multiple instances", think EFS.
- If it says "long retention and rare access", think Glacier.

## What to memorize
| Comparison | Mental rule |
|---|---|
| S3 Standard vs Glacier | Hot Access vs Archiving |
| S3 vs EBS | Object via API vs block for EC2 |
| Versioning vs Lifecycle | Recover history vs optimize lifecycle |

## Next review
After this block, move on to [costs](./costs.md): storage almost always involves cost, retention, and recovery.

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
