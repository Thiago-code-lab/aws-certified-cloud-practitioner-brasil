# Public and Private Subnets

A subnet is public or private according to its routes and the way it accesses the internet, not just its name.

- **Public:** has a direct route to an internet gateway; IPv4 internet access also requires a public IPv4 address and appropriate traffic rules.
- **Private:** has no direct route to an internet gateway.
- Private resources can initiate IPv4 internet connections through a public NAT gateway with appropriate routes.
- **Best practice:** place databases and internal services on private subnets.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> Suggested next step: apply these concepts in data engineering scenarios on AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [Subnet routing and types](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)

- [AWS reference 1](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
