# Security and IAM Deck

<!-- question-id: CLF-FLASH-IAM-001; domain: 2; type: open-response -->
## Card 01
**Question:** Which identity should be protected with MFA and avoided in daily use?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
The AWS account root user. It has broad privileges and should be reserved for exceptional tasks that require root.


[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

<!-- question-id: CLF-FLASH-IAM-002; domain: 2; type: open-response -->
## Card 02
**Question:** In IAM, what is the difference between user and role?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
User represents a persistent identity. Role is assumed temporarily by users, services or accounts, without permanent credentials of their own.


[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

<!-- question-id: CLF-FLASH-IAM-003; domain: 2; type: open-response -->
## Card 03
**Question:** "Least privilege" should appear as which practical decision?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Allow only necessary actions, on the necessary resources, for the necessary time. Broad permission for convenience is a sign of the wrong answer.


[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

<!-- question-id: CLF-FLASH-IAM-004; domain: 2; type: open-response -->
## Card 04
**Question:** An app on EC2 needs to read objects on S3. Which approach is more suitable than saving keys on the server?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Attach an IAM Role to the EC2 instance with least-privilege permissions for the required bucket.


[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

<!-- question-id: CLF-FLASH-IAM-005; domain: 2; type: open-response -->
## Card 05
**Question:** Which service logs API calls to answer "who did what, when, and from where"?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS CloudTrail. It is the classic association for auditing actions in the AWS account.


[AWS reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

</details>

<!-- question-id: CLF-FLASH-IAM-006; domain: 2; type: open-response -->
## Card 06
**Question:** Do AWS Shield, AWS WAF, and security groups protect against the same threats?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. Shield helps against DDoS, WAF filters HTTP/HTTPS web traffic, and Security Groups control network traffic on resources like EC2.


[AWS reference](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)

</details>

<!-- question-id: CLF-FLASH-IAM-007; domain: 2; type: open-response -->
## Card 07
**Question:** Which service centralizes creation and control of encryption keys?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS KMS. KMS manages cryptographic keys and integrates with AWS services; customers still control appropriate permissions and key policies.


[AWS reference](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

</details>

<!-- question-id: CLF-FLASH-IAM-008; domain: 2; type: open-response -->
## Card 08
**Question:** If the test asks for AWS compliance documents and audit reports, which service appears?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS Artifact. It provides access to AWS compliance-related reports and agreements.


[AWS reference](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)

</details>

<!-- question-id: CLF-FLASH-IAM-009; domain: 2; type: open-response -->
## Card 09
**Question:** Can the customer delegate the classification of their own data to AWS?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. Classification, governance, retention and protection of customer data remain the responsibility of the customer.


[AWS reference](https://aws.amazon.com/compliance/shared-responsibility-model/)

</details>

<!-- question-id: CLF-FLASH-IAM-010; domain: 2; type: open-response -->
## Card 10
**Question:** How do an overly broad Allow and an explicit Deny affect IAM access?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
An overly broad Allow increases the attack surface. An applicable explicit Deny overrides an Allow; an excessively broad Deny can also disrupt legitimate work. Evaluate both against least privilege and operational requirements.


[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

<!-- question-id: CLF-FLASH-IAM-011; domain: 2; type: open-response -->
## Card 11
**Question:** Should GuardDuty be remembered as firewall, antivirus or threat detection?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Threat detection. It analyzes events and signals to point out suspicious behavior on the account.


[AWS reference](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

</details>

<!-- question-id: CLF-FLASH-IAM-012; domain: 2; type: open-response -->
## Card 12
**Question:** Common exam mistake: "MFA overrides well-defined IAM policies." Why is it wrong?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
MFA strengthens authentication but does not define authorization. Correct access still depends on policies, roles and least privilege.


[AWS reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
