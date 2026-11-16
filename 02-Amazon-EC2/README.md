# Amazon EC2

Virtual compute module focusing on instances, purchasing models, and basic availability decisions.

## Module focus
- EC2 instances, AMI, instance types, and key pairs.
- EBS as block storage for instances.
- Auto Scaling and Elastic Load Balancing at introductory level.

## Quick review
- EC2 is computing as a service: you choose capacity, system and configuration.
- EBS is persistent block storage, different from S3.
- Auto Scaling adjusts number of instances; Load Balancer distributes traffic.

## Common exam clues
- "Virtual cloud server" -> Amazon EC2.
- "Volume to attach to an instance" -> Amazon EBS.
- "Distribute traffic between instances" -> Elastic Load Balancing.

## Common error
Confusing increasing the size of an instance with high availability. Vertical scaling improves capacity; high availability requires redundancy.

## What to memorize
| Comparison | Exam rule of thumb |
|---|---|
| EC2 vs Lambda | EC2 = customer-managed virtual server; Lambda = serverless execution |
| EBS vs S3 | EBS = block for instance; S3 = objects via API |

## Bridge to next module
After you understand computing, review security: who can create, access, and audit these resources.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


> Practical bridge: After pinning the service, see how it appears in data architectures on AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [AWS reference 2](https://aws.amazon.com/ec2/pricing/)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Lessons and practice

- [Instance Types](01-instance-types.md)
- [Purchasing Options](02-pricing-models.md)
- [Auto Scaling](03-auto-scaling.md)
- [Elastic Load Balancing](04-elastic-load-balancing.md)
- [User Data and Metadata](05-user-data-and-metadata.md)

[Back to all modules](../README.md#modules)
