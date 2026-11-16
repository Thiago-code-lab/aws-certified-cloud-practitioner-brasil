# RDS

Amazon RDS manages relational databases and automates infrastructure provisioning, backups, patches, and replacement.

- Supports popular engines such as PostgreSQL, MySQL, MariaDB, Oracle and SQL Server.
- **Multi-AZ:** increases availability with standby replica.
- **Read Replica:** scales reads; does not replace Multi-AZ.
- **Exam tip:** transactional SQL application with fewer operations points to RDS.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> To study practical data applications after this topic, this Data Engineering course on AWS complements it well: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Multi-AZ deployment types

A traditional Multi-AZ DB instance uses a standby for failover, not read scaling. A Multi-AZ DB cluster has readable standby instances. Read replicas primarily scale reads and have different replication and failover characteristics. Customers still manage schema, queries, access, and appropriate backup settings.

[AWS RDS Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
