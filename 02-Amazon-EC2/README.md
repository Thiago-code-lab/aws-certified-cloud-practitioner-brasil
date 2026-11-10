#Amazon EC2

Virtual compute module focusing on instances, purchasing models, and basic availability decisions.

## Module focus
- EC2 instances, AMI, instance types, and key pairs.
- EBS as block volume for instances.
- Auto Scaling and Elastic Load Balancing at introductory level.

## Quick Review
- EC2 is computing as a service: you choose capacity, system and configuration.
- EBS is persistent block storage, different from S3.
- Auto Scaling adjusts number of instances; Load Balancer distributes traffic.

## Classic proof signals
- "Virtual cloud server" -> Amazon EC2.
- "Volume to attach to an instance" -> Amazon EBS.
- "Distribute traffic between instances" -> Elastic Load Balancing.

## Common error
Confusing increasing the size of an instance with high availability. Vertical scaling improves capacity; High availability requires redundancy.

## What to memorize
| Comparison | Mental rule of proof |
|---|---|
| EC2 vs Lambda | EC2 = customer managed server; Lambda = serverless execution |
| EBS vs S3 | EBS = block for instance; S3 = objects via API |

## Bridge to next module
After you understand computing, review security: who can create, access, and audit these resources.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil


> Practical bridge: After pinning the service, see how it appears in data architectures on AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
