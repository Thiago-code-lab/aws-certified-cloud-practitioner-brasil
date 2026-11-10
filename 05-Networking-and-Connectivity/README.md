# Networks and Connectivity

Module to recognize the most charged network services at the Cloud Practitioner level.

## Module focus
- VPC, subnets, Security Groups and NACLs.
- Route 53, CloudFront and high-level hybrid connectivity.
- Public, private and edge network concepts.

## Quick Review
- VPC logically isolates network resources in AWS.
- Security Group operates at the resource level; NACL operates at the subnet level.
- CloudFront brings user content closer to edge locations.

## Classic proof signals
- "Managed DNS" -> Amazon Route 53.
- "Deliver content with global low latency" -> Amazon CloudFront.
- "Dedicated connection between datacenter and AWS" -> AWS Direct Connect.

## Common error
Treat Security Group and NACL as equal. Security Group is stateful; NACL is stateless.

## What to memorize
| Comparison | Mental rule of proof |
|---|---|
| Security Group vs NACL | SG protects resource; NACL protects subnet |
| Route 53 vs CloudFront | Route 53 resolves DNS; CloudFront delivers content |

## Bridge to next module
With the network understood, move on to the database: where the application stores structured data and how this affects operations.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil


> Optional Deep Dive: To bring this concept to data projects on AWS, use as a next step: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
