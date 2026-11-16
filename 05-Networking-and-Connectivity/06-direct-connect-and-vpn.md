# Direct Connect and VPN

AWS Site-to-Site VPN and AWS Direct Connect connect an on-premises network to AWS.

- **VPN:** encrypted tunnel over the internet, quick to deploy.
- **Direct Connect:** dedicated private connection, with more predictable performance and slower deployment.
- The two can be combined for resiliency.
- **Exam tip:** short term points to VPN; constant, predictable traffic points to Direct Connect.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


---

## Encryption distinction

A dedicated connection does not automatically mean encrypted traffic. Direct Connect traffic is not encrypted by default; use supported MACsec or an appropriate VPN design when encryption is required.

[AWS Direct Connect encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html)

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
