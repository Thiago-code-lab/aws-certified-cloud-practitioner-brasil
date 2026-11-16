# Policies and ACLs

Access to S3 can be controlled with IAM policies, bucket policies, access points, and ACLs.

- **IAM Policy:** defines what an identity can do.
- **Bucket policy:** resource-based rule, useful for cross-account access.
- **ACL:** legacy access-control mechanism; prefer policies in most cases.
- Keep public access blocking active when public access is not required.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> When this subject appears in data scenarios, it is worth reviewing the Data Engineering on AWS course: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Current access defaults

New general purpose buckets use Bucket owner enforced Object Ownership with ACLs disabled by default. Keep S3 Block Public Access enabled and use IAM and bucket policies for access.

[AWS Object Ownership documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [AWS reference 2](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
