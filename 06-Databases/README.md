# Databases

Module to differentiate the main data services at the introductory level of the CLF-C02.

## Module focus
- Amazon RDS for managed relational databases.
- DynamoDB for NoSQL key-value/document.
- Redshift for analytics and data warehousing.

## Quick review
- RDS reduces operational work in relational databases.
- DynamoDB appears when the scenario requires NoSQL, low latency and managed scale.
- Redshift is associated with analytics and data warehousing.

## Common exam clues
- "Managed relational database" -> Amazon RDS.
- "NoSQL serverless with low latency" -> Amazon DynamoDB.
- "Large volume analysis of structured data" -> Amazon Redshift.

## Common error
Choose RDS just because you know SQL when the statement asks for NoSQL scaling or key-value access.

## What to memorize
| Comparison | Exam rule of thumb |
|---|---|
| RDS vs DynamoDB | RDS = relational; DynamoDB = Managed NoSQL |
| RDS vs Redshift | RDS = transactional; Redshift = analysis |

## Bridge to next module
After data, move on to serverless: how to run code and integrate events with less operational effort.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


> For additional practice with AWS data projects, explore this course: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Lessons and practice

- [RDS](01-rds.md)
- [Aurora](02-aurora.md)
- [DynamoDB](03-dynamodb.md)
- [ElastiCache](04-elasticache.md)
- [Redshift](05-redshift.md)
- [DocumentDB and Neptune](06-documentdb-and-neptune.md)
- [Database Migration Service](07-database-migration-service.md)

[Back to all modules](../README.md#modules)
