# Monitoring and Governance

Module to review observability, auditing and organizational control at an entry level.

## Module focus
- CloudWatch for metrics, logs and alarms.
- CloudTrail for API auditing.
- AWS Organizations and Tags for basic governance.

## Quick Review
- CloudWatch observes performance and operational behavior.
- CloudTrail records actions on the account for auditing.
- Tags help organize cost, owner and environment.

## Common exam clues
- "Create metric alarm" -> Amazon CloudWatch.
- "Who called an API" -> AWS CloudTrail.
- "Manage multiple accounts" -> AWS Organizations.

## Common error
Confusing CloudWatch with CloudTrail. CloudWatch monitors operation; CloudTrail audits actions.

## What to memorize
| Comparison | Exam rule of thumb |
|---|---|
| CloudWatch vs CloudTrail | Operational metrics/logs vs audit trail |
| Tags vs Organizations | Tags organize resources; Organizations organizes accounts |

## Bridge to next module
After governance, review costs: monitoring only becomes control when spent and alerts enter the cycle.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


> Practical bridge: After pinning the service, see how it appears in data architectures on AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Lessons and practice

- [CloudWatch](01-cloudwatch.md)
- [CloudTrail](02-cloudtrail.md)
- [AWS Config](03-aws-config.md)
- [AWS Trusted Advisor](04-aws-trusted-advisor.md)
- [AWS Health Dashboard](05-aws-health-dashboard.md)
- [AWS Systems Manager](06-aws-systems-manager.md)
- [AWS Compute Optimizer](07-aws-compute-optimizer.md)

[Back to all modules](../README.md#modules)
