# 10-Question Practice Exam

10 reviewed questions. Each question has one correct answer and four alternatives.

A short supplementary exercise, not a full-length exam or a weighted exam simulation. The official exam has 65 questions; this exercise has 10.
<!-- question-id: CLF-MOCK-001; domain: 1; select: 1 -->
## Question 1

A company needs to rapidly add resources during peaks and release them afterward. Which cloud benefit describes this? Select one answer.

A) Immutability

B) Elasticity

C) Dedicated physical isolation

D) Fixed latency

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** Immutability concerns replacing rather than modifying resources.

- **B — Correct:** Elasticity matches capacity to changing demand, including scaling back down.

- **C — Incorrect:** Dedicated isolation concerns tenancy, not matching capacity to load.

- **D — Incorrect:** Cloud services do not promise universally fixed latency.

**Official domain:** 1.

[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

---

<!-- question-id: CLF-MOCK-002; domain: 2; select: 1 -->
## Question 2

Which service provides an audit trail of supported account actions? Select one answer.

A) CloudTrail

B) S3

C) EBS

D) Athena

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** CloudTrail records supported account activity as events.

- **B — Incorrect:** S3 can store CloudTrail logs, but does not itself capture account API activity.

- **C — Incorrect:** EBS stores block data for EC2.

- **D — Incorrect:** Athena queries data and can analyze logs, but is not the event recording service.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

</details>

---

<!-- question-id: CLF-MOCK-003; domain: 3; select: 1 -->
## Question 3

Which option is a managed relational database service? Select one answer.

A) DynamoDB

B) RDS

C) ElastiCache

D) S3

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** DynamoDB is a NoSQL key-value and document database.

- **B — Correct:** RDS provides managed relational databases.

- **C — Incorrect:** ElastiCache provides in-memory caching.

- **D — Incorrect:** S3 provides object storage.

**Official domain:** 3.

[AWS reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

</details>

---

<!-- question-id: CLF-MOCK-004; domain: 4; select: 1 -->
## Question 4

Which tool supports tracking and forecasting AWS costs? Select one answer.

A) Cost Explorer

B) KMS

C) Route 53

D) ECS

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** Cost Explorer analyzes cost and usage and provides forecasts subject to available history.

- **B — Incorrect:** KMS manages encryption keys.

- **C — Incorrect:** Route 53 provides DNS and related services.

- **D — Incorrect:** ECS orchestrates containers.

**Official domain:** 4.

[AWS reference](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)

</details>

---

<!-- question-id: CLF-MOCK-005; domain: 2; select: 1 -->
## Question 5

Under the Shared Responsibility Model, who sets the password policy for IAM users in a customer account? Select one answer.

A) AWS

B) The customer

C) AWS Support by default

D) A training partner by default

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** AWS manages cloud infrastructure, not the customer's IAM user password policy.

- **B — Correct:** The customer configures IAM account password requirements; federated identities instead use their identity provider's policies.

- **C — Incorrect:** Support does not automatically administer customer identity settings.

- **D — Incorrect:** A training relationship does not grant account administration permissions.

**Official domain:** 2.

[AWS reference](https://aws.amazon.com/compliance/shared-responsibility-model/)

</details>

---

<!-- question-id: CLF-MOCK-006; domain: 3; select: 1 -->
## Question 6

Which service stores objects and static content? Select one answer.

A) S3

B) Aurora

C) EC2 Auto Scaling

D) IAM

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** S3 stores objects including static website assets.

- **B — Incorrect:** Aurora is a relational database.

- **C — Incorrect:** EC2 Auto Scaling manages instance group capacity.

- **D — Incorrect:** IAM controls identities and access.

**Official domain:** 3.

[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

</details>

---

<!-- question-id: CLF-MOCK-007; domain: 1; select: 1 -->
## Question 7

Which approach generally improves web application availability? Select one answer.

A) One instance in one Availability Zone

B) Instances across multiple Availability Zones

C) No backups

D) No monitoring

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** A single instance and zone introduce single points of failure.

- **B — Correct:** A multi-zone design with appropriate routing and failover reduces localized failure impact.

- **C — Incorrect:** Removing backups undermines recovery.

- **D — Incorrect:** Removing monitoring delays failure detection.

**Official domain:** 1.

[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

---

<!-- question-id: CLF-MOCK-008; domain: 3; select: 1 -->
## Question 8

Which service runs function code without the customer managing servers? Select one answer.

A) Lambda

B) EC2

C) Redshift

D) Direct Connect

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** Lambda manages the underlying function execution infrastructure.

- **B — Incorrect:** EC2 generally requires management of instances and guest operating systems.

- **C — Incorrect:** Redshift is an analytical database service.

- **D — Incorrect:** Direct Connect provides dedicated network connectivity.

**Official domain:** 3.

[AWS reference](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

</details>

---

<!-- question-id: CLF-MOCK-009; domain: 2; select: 1 -->
## Question 9

Which root user security practice is recommended? Select one answer.

A) Share root credentials with the team

B) Disable MFA

C) Enable MFA and limit root use

D) Create root access keys for automation

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** C

- **A — Incorrect:** Shared root credentials expose highly privileged access.

- **B — Incorrect:** Disabling MFA weakens authentication.

- **C — Correct:** Protect root with MFA and use it only for tasks that require it; prefer federated roles for routine work.

- **D — Incorrect:** Use roles and temporary credentials rather than root access keys.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

---

<!-- question-id: CLF-MOCK-010; domain: 4; select: 1 -->
## Question 10

Which tool can notify you when actual or forecast spending crosses a configured threshold? Select one answer.

A) AWS Budgets

B) AWS Artifact

C) AWS Config

D) CloudFront

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** Budgets supports cost, usage, and commitment monitoring and notifications; data updates and delivery can be delayed.

- **B — Incorrect:** Artifact provides compliance reports and agreements.

- **C — Incorrect:** Config records resource configurations and evaluates rules.

- **D — Incorrect:** CloudFront delivers cached content at edge locations.

**Official domain:** 4.

[AWS reference](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

</details>

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
