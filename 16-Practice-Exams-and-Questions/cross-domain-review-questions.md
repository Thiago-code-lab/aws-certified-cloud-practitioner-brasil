# Cross Domain Review Questions

6 reviewed questions. Each question has one correct answer and four alternatives.

Supplementary practice across the four official CLF-C02 domains. This is not an additional exam domain.
<!-- question-id: CLF-CROSS-001; domain: 2; select: 1 -->
## Question 1

Which service is global within an AWS partition and manages identities and permissions? Select one answer.

A) IAM

B) EC2

C) EBS

D) RDS

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** IAM identities are not created separately in each Region; partitions such as standard AWS and AWS China are distinct.

- **B — Incorrect:** EC2 instances are placed in an Availability Zone within a Region.

- **C — Incorrect:** EBS volumes are associated with an Availability Zone.

- **D — Incorrect:** RDS database resources are Regional.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

---

<!-- question-id: CLF-CROSS-002; domain: 3; select: 1 -->
## Question 2

Which service most directly stores static website files? Select one answer.

A) Amazon S3

B) Amazon DynamoDB

C) AWS Organizations

D) AWS KMS

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** S3 stores static objects; for secure public delivery, use CloudFront with a private S3 bucket origin and origin access control.

- **B — Incorrect:** DynamoDB is a database, not static website hosting.

- **C — Incorrect:** Organizations manages accounts and policies.

- **D — Incorrect:** KMS manages encryption keys.

**Official domain:** 3.

[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

</details>

---

<!-- question-id: CLF-CROSS-003; domain: 2; select: 1 -->
## Question 3

Which combination reduces account compromise risk? Select one answer.

A) Disable MFA

B) Use root for everyday work

C) Enable MFA and use appropriately scoped IAM roles

D) Publish access keys in a repository

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** C

- **A — Incorrect:** Disabling MFA weakens authentication.

- **B — Incorrect:** Daily root use unnecessarily exposes the most privileged identity.

- **C — Correct:** MFA and least-privilege roles with temporary credentials reduce credential and authorization risk.

- **D — Incorrect:** Published keys can be abused and must be revoked if exposed.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

---

<!-- question-id: CLF-CROSS-004; domain: 1; select: 1 -->
## Question 4

What is a benefit of distributing an application across multiple Availability Zones? Select one answer.

A) Eliminate network costs

B) Improve availability

C) Remove the need for monitoring

D) Replace IAM

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** Cross-zone traffic may still incur charges.

- **B — Correct:** A suitably designed multi-zone application can continue operating after a localized failure.

- **C — Incorrect:** Redundant deployments still require monitoring.

- **D — Incorrect:** Availability design does not replace identity and access controls.

**Official domain:** 1.

[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

---

<!-- question-id: CLF-CROSS-005; domain: 4; select: 1 -->
## Question 5

Which combination provides initial cost visibility and spending alerts? Select one answer.

A) Cost Explorer and AWS Budgets

B) CloudTrail and Route 53

C) IAM and KMS

D) WAF and Shield

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** Cost Explorer analyzes spending; Budgets provides threshold notifications.

- **B — Incorrect:** CloudTrail records account actions and Route 53 provides DNS.

- **C — Incorrect:** IAM manages access and KMS manages encryption keys.

- **D — Incorrect:** WAF and Shield protect applications and help address DDoS threats; they are not cost analysis and budget tools.

**Official domain:** 4.

[AWS reference](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)

</details>

---

<!-- question-id: CLF-CROSS-006; domain: 3; select: 1 -->
## Question 6

Which service runs short event-driven function code without requiring server management? Select one answer.

A) AWS Lambda

B) AWS Snow Family

C) Amazon Redshift

D) AWS Storage Gateway

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** Lambda runs function code in response to events with AWS-managed compute infrastructure.

- **B — Incorrect:** Snow Family refers to physical transfer and edge device offerings, not managed event functions.

- **C — Incorrect:** Redshift performs data warehouse analytics.

- **D — Incorrect:** Storage Gateway connects on-premises storage interfaces to AWS storage.

**Official domain:** 3.

[AWS reference](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

</details>

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
