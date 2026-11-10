# Serverless Computing

Module for recognizing serverless services and simple event-driven patterns.

## Module focus
- AWS Lambda for on-demand code execution.
- API Gateway as input for APIs.
- SQS and SNS as decoupled integration.

## Quick Review
- Lambda runs code without provisioning server.
- API Gateway exposes APIs and can trigger Lambda.
- SQS queues messages; SNS publishes notifications to subscribers.

## Classic proof signals
- "Execute short code in response to event" -> AWS Lambda.
- "Create managed API endpoint" -> Amazon API Gateway.
- "Decouple components with queue" -> Amazon SQS.

## Common error
Choose EC2 for simple event-driven tasks when the statement requires smaller operations.

## What to memorize
| Comparison | Mental rule of proof |
|---|---|
| Lambda vs EC2 | Lambda = serverless event; EC2 = configurable server |
| SQS vs SNS | SQS = queue; SNS = publication/notification |

## Bridge to next module
After serverless, review general storage: correct choice between object, block and file.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil


> When this subject appears in data scenarios, it is worth reviewing the Data Engineering on AWS course: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
