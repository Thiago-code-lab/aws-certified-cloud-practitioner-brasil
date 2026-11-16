# Networks and Connectivity

Module for recognizing commonly tested networking services at the Cloud Practitioner level.

## Module focus
- VPC, subnets, Security Groups and NACLs.
- Route 53, CloudFront and high-level hybrid connectivity.
- Public, private and edge network concepts.

## Quick review
- VPC logically isolates network resources in AWS.
- Security Group operates at the resource level; NACL operates at the subnet level.
- CloudFront caches content at edge locations closer to users.

## Common exam clues
- "Managed DNS" -> Amazon Route 53.
- "Deliver content with global low latency" -> Amazon CloudFront.
- "Dedicated connection between datacenter and AWS" -> AWS Direct Connect.

## Common error
Treating security groups and network ACLs as interchangeable. Security Group is stateful; NACL is stateless.

## What to memorize
| Comparison | Exam rule of thumb |
|---|---|
| Security Group vs NACL | SG protects resource; NACL protects subnet |
| Route 53 vs CloudFront | Route 53 resolves DNS; CloudFront delivers content |

## Bridge to next module
With the network understood, move on to the database: where the application stores structured data and how this affects operations.

## Continuity
Architecture Track: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


> Optional Deep Dive: To bring this concept to data projects on AWS, use as a next step: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Lessons and practice

- [VPC Fundamentals](01-vpc-fundamentals.md)
- [Public and Private Subnets](02-public-and-private-subnets.md)
- [Internet Gateway and NAT](03-internet-gateway-and-nat.md)
- [Security Groups and Network ACLs](04-security-groups-and-network-acls.md)
- [VPC Peering and Transit Gateway](05-vpc-peering-and-transit-gateway.md)
- [Direct Connect and VPN](06-direct-connect-and-vpn.md)
- [Route 53](07-route-53.md)

[Back to all modules](../README.md#modules)
