# EBS

Amazon EBS provides persistent block volumes, primarily used by EC2 instances.

- It is suitable for file systems, databases and boot disks.
- The volume belongs to an AZ and can survive instance termination.
- Snapshots enable backup and restore.
- **Exam tip:** persistent disk for EC2 points to EBS; objects point to S3.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> Career complement: anyone who wants to move from the cloud fundamentals to real data projects can follow here: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Persistence depends on deletion settings

An EBS volume is tied to one Availability Zone. Its survival after instance termination depends on `DeleteOnTermination`; root EBS volumes are deleted by default in typical configurations. Snapshots allow new volumes to be created in another zone. EBS Multi-Attach is a restricted feature for supported volume types and clustered applications, not a general shared file system.

[AWS EBS volume preservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/preserving-volumes-on-termination.html)

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
