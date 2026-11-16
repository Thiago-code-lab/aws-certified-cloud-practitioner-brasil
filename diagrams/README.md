# Architecture Diagrams

Short-form supporting content for objective review and initial application.

## How to use
- Read in blocks of 10 to 20 minutes.
- Mark questions to review in the main module.
- Reinforce the topics with the highest incidence of errors.

## Recommended evolution
AWS Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english
AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## Diagram interpretation

[Basic architecture](basic-architecture.svg) shows static delivery through CloudFront with S3 storage; use a private S3 REST origin and OAC for the secured pattern. [Security flow](security-flow.svg) shows complementary controls, not an automatically configured pipeline: CloudTrail events require an explicit monitoring integration, such as CloudWatch Logs metric filters and alarms or EventBridge rules, to trigger notifications.

[AWS CloudTrail monitoring with CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)


## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
