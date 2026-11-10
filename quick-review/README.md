# Quick Review - CLF-C02

Use this block for 20-30 minute sessions, focused by domain. It doesn't replace flashcards: here the idea is to quickly diagnose gaps before returning to the right module.

## Review by domain
| Domain | Short Review | When to use |
|---|---|---|
| Cloud Fundamentals | [fundamentals.md](./fundamentals.md) | When to make a mistake Region, AZ, elasticity or shared responsibility |
| IAM and security | [security.md](./security.md) | When you get identity, permissions, auditing or compliance wrong |
| S3 and Storage | [storage.md](./storage.md) | When you make a mistake S3, EBS, EFS, classes or lifecycle |
| Costs and pricing | [costs.md](./costs.md) | When you get it wrong Budgets, Cost Explorer, Spot, support or pricing models |

## Suggested flow
1. Run the [eve checklist](./exam-eve-checklist.md).
2. Review the domain with the highest error using the files above.
3. See [key services](./key-services.md) for quick comparison.
4. Reread [common errors](./common-mistakes.md) before solving new questions.

## Mini diagnostic training

### Question 1
An application must remain available if an isolated data center in the Region fails. Which design best meets the CLF-C02 level?

A) Multi-AZ  
B) Root user with MFA  
C) S3 Glacier Deep Archive  
D) AWS Budgets

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

**Explanation:**
Multi-AZ distributes resources across Availability Zones and is the most direct association for regional high availability.

</details>

### Question 2
A team wants to allow an EC2 application to access an S3 bucket without storing access keys on the server. Which option is most suitable?

A) IAM Role for instance  
B) AWS Artifact  
C) Developer support plan  
D) S3 Lifecycle

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

**Explanation:**
IAM Role provides temporary credentials and controlled permissions for the application, reducing operational risk.

</details>

### Question 3
Log files must be kept for years, almost never accessed, and can take hours to retrieve. Which choice is more coherent?

A) S3 Glacier Deep Archive  
B) S3 Standard  
C) EBS gp3  
D) EC2 On-Demand

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

**Explanation:**
Glacier Deep Archive is aimed at long retention, very rare access and low cost, accepting longer recovery.

</details>

### Question 4
Before launching an architecture, the company wants to estimate monthly how much it should cost. Which tool to use?

A) AWS Pricing Calculator  
B) AWS CloudTrail  
C) Amazon GuardDuty  
D) S3 Transfer Acceleration

<details>
<summary><strong>View answer</strong></summary>

**Correct answer:** A

**Explanation:**
Pricing Calculator estimates planned cost before use. To analyze expenses that have already occurred, the association would be Cost Explorer.

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
