# Deck Security and IAM

## Card 01
**Question:** Which account should be protected with MFA and avoided in daily use?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
The root account. It has broad privileges and should be reserved for exceptional tasks that require root.

</details>

## Card 02
**Question:** In IAM, what is the difference between user and role?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
User represents a persistent identity. Role is assumed temporarily by users, services or accounts, without permanent credentials of their own.

</details>

## Card 03
**Question:** "Least privilege" should appear as which practical decision?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Allow only necessary actions, on the necessary resources, for the necessary time. Broad permission for convenience is a sign of the wrong answer.

</details>

## Card 04
**Question:** An app on EC2 needs to read objects on S3. Which approach is more suitable than saving keys on the server?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Attach an IAM Role to the EC2 instance with minimum permissions for the required bucket.

</details>

## Card 05
**Question:** Which service logs API calls to answer "who did what, when, and from where"?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS CloudTrail. It is the classic association for auditing actions in the AWS account.

</details>

## Card 06
**Question:** AWS Shield, WAF and Security Groups protect exactly the same thing?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. Shield helps against DDoS, WAF filters HTTP/HTTPS web traffic, and Security Groups control network traffic on resources like EC2.

</details>

## Card 07
**Question:** Which service centralizes creation and control of encryption keys?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS KMS. Remember how the managed key service for encryption integrated with AWS services.

</details>

## Card 08
**Question:** If the test asks for AWS compliance documents and audit reports, which service appears?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS Artifact. It provides access to AWS compliance-related reports and agreements.

</details>

## Card 09
**Question:** Can the customer delegate the classification of their own data to AWS?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. Classification, governance, retention and protection of customer data remains the responsibility of the customer.

</details>

## Card 10
**Question:** Which error is more dangerous: explicit Deny policy or too broad Allow?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Allow too wide increases scratch surface. In IAM, an explicit Deny typically prevails and blocks access.

</details>

## Card 11
**Question:** Should GuardDuty be remembered as firewall, antivirus or threat detection?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Threat detection. It analyzes events and signals to point out suspicious behavior on the account.

</details>

## Card 12
**Question:** Common proof error: "MFA overrides well-defined IAM policies." Why is it wrong?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
MFA strengthens authentication but does not define authorization. Correct access still depends on policies, roles and least privilege.

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
