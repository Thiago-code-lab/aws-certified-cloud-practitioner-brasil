# Security Groups and Network ACLs

Security Groups and Network ACLs filter traffic at different layers of the VPC.

- **Security Group:** applies to associated resources, is stateful, and supports allow rules only. Return traffic for allowed connections is automatically permitted.
- **NACL:** applies at the subnet boundary, is stateless, and supports allow and deny rules. Inbound and outbound rules must explicitly permit the required traffic, including return traffic.
- Security Groups are the primary control for instances and interfaces.
- **Exam tip:** explicit block by subnet points to NACL.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> Complementary resource: if you want to connect this foundation with pipelines and analytics in AWS, see the Data Engineering in AWS course: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [Network ACL behavior](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

- [AWS reference 1](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
