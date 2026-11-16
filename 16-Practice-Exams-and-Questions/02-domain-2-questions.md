# Domain 2 Questions

6 reviewed questions. Each question has one correct answer and four alternatives.
<!-- question-id: CLF-D2-001; domain: 2; select: 1 -->
## Question 1

Under the Shared Responsibility Model, who configures IAM permissions in a customer account? Select one answer.

A) AWS

B) The customer

C) A billing partner by default

D) An external auditor by default

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** AWS secures the underlying cloud infrastructure; it does not choose the customer's identity policies.

- **B — Correct:** The customer controls account identities, access policies, and permissions.

- **C — Incorrect:** A billing relationship does not automatically delegate IAM administration.

- **D — Incorrect:** An auditor evaluates controls; administration requires explicit delegated permissions.

**Official domain:** 2.

[AWS reference](https://aws.amazon.com/compliance/shared-responsibility-model/)

</details>

---

<!-- question-id: CLF-D2-002; domain: 2; select: 1 -->
## Question 2

Which practice follows the principle of least privilege? Select one answer.

A) Give every team member administrator access

B) Grant only the permissions required for each role

C) Share the root user

D) Disable MFA to simplify sign-in

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** Broad administrator access exceeds most users' needs.

- **B — Correct:** Permissions should be limited to the actions and resources needed for the task.

- **C — Incorrect:** Sharing root credentials removes individual accountability and grants excessive privilege.

- **D — Incorrect:** Disabling MFA weakens authentication rather than limiting permissions.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

---

<!-- question-id: CLF-D2-003; domain: 2; select: 1 -->
## Question 3

Which service records account activity for auditing? Select one answer.

A) AWS CloudTrail

B) Amazon Route 53

C) AWS Budgets

D) Amazon EFS

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** CloudTrail records supported account actions as events, including API activity.

- **B — Incorrect:** Route 53 provides DNS, domain registration, and health checks.

- **C — Incorrect:** Budgets tracks financial and usage thresholds.

- **D — Incorrect:** EFS provides shared file storage.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

</details>

---

<!-- question-id: CLF-D2-004; domain: 2; select: 1 -->
## Question 4

Which combination is appropriate for securely storing application secrets and controlling access? Select one answer.

A) A public S3 bucket with an open ACL

B) AWS Secrets Manager with IAM

C) An EC2 instance without encryption

D) A manual local snapshot

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** Public access would expose confidential credentials.

- **B — Correct:** Secrets Manager stores secrets and integrates with IAM for access control; use supported rotation where appropriate.

- **C — Incorrect:** An unencrypted instance alone provides neither secret lifecycle management nor suitable access controls.

- **D — Incorrect:** A local snapshot is a backup mechanism, not a managed secret retrieval and access solution.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

</details>

---

<!-- question-id: CLF-D2-005; domain: 2; select: 1 -->
## Question 5

Which action improves root user security? Select one answer.

A) Share the password with the team

B) Enable MFA

C) Disable logging

D) Create permanent root access keys

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** Shared credentials increase exposure and reduce accountability.

- **B — Correct:** MFA strengthens root authentication; reserve root for tasks that require it.

- **C — Incorrect:** Disabling logs reduces detection and auditability.

- **D — Incorrect:** Root access keys grant highly privileged programmatic access and should not be created.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

---

<!-- question-id: CLF-D2-006; domain: 2; select: 1 -->
## Question 6

Which service continuously analyzes AWS data sources to detect threats? Select one answer.

A) Amazon GuardDuty

B) AWS Snowball

C) Amazon SQS

D) AWS Artifact

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** GuardDuty analyzes supported data sources to identify suspicious activity and threats.

- **B — Incorrect:** Snowball is a physical data transfer and edge device offering, not a threat detection service.

- **C — Incorrect:** SQS is a message queue.

- **D — Incorrect:** Artifact provides access to compliance reports and agreements.

**Official domain:** 2.

[AWS reference](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

</details>

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
