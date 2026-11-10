# Questions Domain 2 - Security and Compliance

## Question 1
In the shared responsibility model, who sets up account IAM permissions?

A) AWS
B) Customer
C) Billing partner
D) External auditor

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:**
The customer is responsible for identity and permissions on the account.

**Why is option A wrong:**
AWS protects infrastructure, does not define customer policies.

</details>

---

## Question 2
Which practice follows the principle of least privilege?

A) Give administrator access to the entire team
B) Give only necessary permissions per role
C) Share root user
D) Remove MFA to make login easier

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:**
Least privilege reduces risk surface.

**Why is option A wrong:**
Pervasive full access increases operational risk.

</details>

---

## Question 3
Which service is most associated with auditing actions in the AWS account?

A) AWS CloudTrail
B) Amazon Route 53
C) AWS Budgets
D) Amazon EFS

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
CloudTrail logs API calls and governance events.

**Why option B is wrong:**
Route 53 is DNS, not audit trail.

</details>

---

## Question 4
To protect application secrets (passwords/keys), which combination is most common?

A) Public S3 + open ACL
B) Secrets Manager + IAM
C) EC2 without encryption
D) Local manual snapshot

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:**
Secrets Manager centralizes and protects secrets with access control.

**Why is option A wrong:**
Public exposure of sensitive data is an unsafe practice.

</details>

---

## Question 5
Which measure increases root account security?

A) Share password with team
B) Enable MFA
C) Disable logs
D) Create permanent access keys for root

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** B

**Explanation:**
MFA adds second layer of authentication.

**Why option D is wrong:**
Permanent root keys increase severe risk.

</details>

---

## Question 6
Which service helps detect threats with continuous analysis?

A) Amazon GuardDuty
B) AWS Snowball
C) Amazon SQS
D) AWS Artifact

<details>
<summary><strong>View answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
GuardDuty identifies suspicious behavior and potential threats.

**Why option C is wrong:**
SQS is message queuing, not threat detection.

</details>



> Complementary track: cloud fundamentals become clearer when applied to data pipelines in AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
