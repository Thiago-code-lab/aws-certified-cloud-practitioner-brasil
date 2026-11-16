# IAM

## Identities

- **User:** long-term identity; use only when necessary.
- **Group:** brings together users with similar permissions.
- **Role:** provides temporary credentials for people, services and applications.
- **Federation:** uses an external identity provider for access to AWS.

## Policies

- A policy defines allowed or denied actions, resources, and conditions.
- An explicit deny takes precedence over permissions.
- SCP limits the maximum allowed on Organizations accounts, but does not grant access.

## Good practices

- Enable MFA, apply least privilege, and review credentials.
- Avoid permanent access keys and never use the root user for daily work.
- Do not store secrets in code; use dedicated services such as AWS Secrets Manager for credentials and rotation.

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english
AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

Prefer federation for workforce access and roles for workloads. A role itself is persistent; the credentials obtained by assuming it expire. An applicable explicit Deny overrides an Allow.
