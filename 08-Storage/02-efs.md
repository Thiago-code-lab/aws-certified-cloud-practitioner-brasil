# EFS

Amazon EFS provides an elastic, shared file system for Linux workloads using NFS.

- Multiple instances can mount the same system at the same time.
- Capacity grows and shrinks automatically.
- Can be accessed by resources in multiple AZs.
- **Exam tip:** files shared by Linux instances point to EFS; individual disk points to EBS.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> Practical bridge: After pinning the service, see how it appears in data architectures on AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Regional and One Zone storage

EFS Regional file systems provide resilience across multiple Availability Zones. EFS One Zone file systems store data within a single AZ and have a different availability and resilience profile. Do not assume every EFS file system stores data across zones.

[AWS EFS storage classes](https://docs.aws.amazon.com/efs/latest/ug/features.html)

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
