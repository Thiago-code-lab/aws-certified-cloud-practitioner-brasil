# AWS X-Ray

AWS X-Ray helps track requests in distributed applications and locate bottlenecks and failures.

- A trace shows the call path between components.
- Segments display timing, errors, and dependencies.
- Supplements CloudWatch metrics and logs.
- **Exam tip:** finding out where a request was slow between microservices points to X-Ray.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> Practical bridge: After pinning the service, see how it appears in data architectures on AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Availability and scope review — November 10, 2026

The X-Ray SDKs and daemon entered maintenance mode on February 25, 2026, and the current support timeline lists maintenance mode without an end date. Do not reuse older notices that announced a February 2027 end date. AWS recommends OpenTelemetry instrumentation. This lifecycle notice concerns the SDKs and daemon, not a declaration that the X-Ray service is retired.

[AWS lifecycle reference](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html)

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

[AWS current X-Ray SDK and daemon support timeline](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html)
