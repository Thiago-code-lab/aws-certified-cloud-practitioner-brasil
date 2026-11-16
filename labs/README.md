# Hands-on Labs

This directory brings together short labs to turn CLF-C02 concepts into practice. Do them in a study account, use the Region indicated in each step and remove the resources when finished.

## Suggested order

1. **Initial IAM:** understand a temporary read-only identity without using the root account.
2. **Static website on S3:** publish files and understand object permissions.
3. **Basic CloudWatch:** observe metrics and set an alarm.

## Before you begin

- Enable MFA on the root account and configure a low spending budget alert.
- Use easy-to-find names and tags like `Project=cloud-practitioner-labs`.
- Never publish keys, passwords or personal data.
- When finished, confirm on the console that the charged resources have been deleted.

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english
AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

## Reviewed lab procedures

All labs received static documentation review only; no AWS infrastructure was provisioned or runtime validation claimed.

- [Initial IAM setup](lab-01-iam-setup.md): temporary read-only user and group, root MFA, and federation guidance.
- [S3 and CloudFront static website](lab-02-s3-static-website.md): private REST origin, OAC, and HTTPS.
- [Basic CloudWatch monitoring](lab-03-basic-cloudwatch.md): existing resource metrics and monitoring-only alarm.
