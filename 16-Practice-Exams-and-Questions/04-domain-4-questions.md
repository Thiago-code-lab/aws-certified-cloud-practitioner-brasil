# Domain 4 Questions

6 reviewed questions. Each question has one correct answer and four alternatives.
<!-- question-id: CLF-D4-001; domain: 4; select: 1 -->
## Question 1

Which EC2 purchasing option fits an unpredictable workload that cannot tolerate Spot capacity-reclamation interruptions without a long-term commitment? Select one answer.

A) Savings Plans

B) A long-term Reserved Instance commitment

C) On-Demand

D) Spot only

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** C

- **A — Incorrect:** Savings Plans require a one- or three-year usage commitment.

- **B — Incorrect:** Reserved Instances involve a term commitment.

- **C — Correct:** On-Demand does not require a long-term commitment and avoids the capacity-reclamation interruptions associated with Spot; it does not guarantee uninterrupted service or unlimited capacity.

- **D — Incorrect:** Spot capacity can be reclaimed, conflicting with the interruption requirement.

**Official domain:** 4.

[AWS reference](https://aws.amazon.com/ec2/pricing/)

</details>

---

<!-- question-id: CLF-D4-002; domain: 4; select: 1 -->
## Question 2

Which tool helps visualize historical costs by service and time period? Select one answer.

A) AWS Cost Explorer

B) AWS Shield

C) Amazon VPC

D) AWS Lambda

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** Cost Explorer analyzes cost and usage history and trends.

- **B — Incorrect:** Shield provides DDoS protection.

- **C — Incorrect:** VPC provides isolated virtual networking.

- **D — Incorrect:** Lambda executes application code.

**Official domain:** 4.

[AWS reference](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)

</details>

---

<!-- question-id: CLF-D4-003; domain: 4; select: 1 -->
## Question 3

Which tool supports alerts when spending approaches a configured threshold? Select one answer.

A) AWS Budgets

B) Amazon Inspector

C) AWS WAF

D) AWS Glue

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** A

- **A — Correct:** Budgets can notify on actual or forecast cost thresholds; alerts are not an automatic spending cap.

- **B — Incorrect:** Inspector assesses supported resources for vulnerabilities.

- **C — Incorrect:** WAF filters web traffic.

- **D — Incorrect:** Glue provides data integration.

**Official domain:** 4.

[AWS reference](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

</details>

---

<!-- question-id: CLF-D4-004; domain: 4; select: 1 -->
## Question 4

A workload tolerates interruption and seeks discounted EC2 capacity. Which option should be considered? Select one answer.

A) On-Demand

B) Spot Instances

C) Dedicated Hosts

D) Enterprise Support

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** On-Demand offers flexibility but does not use the discounted spare-capacity model.

- **B — Correct:** Spot offers discounted spare capacity that AWS can reclaim; the workload must handle interruption.

- **C — Incorrect:** Dedicated Hosts provide dedicated physical capacity for requirements such as licensing and isolation.

- **D — Incorrect:** Enterprise Support is a support plan, not an EC2 purchasing option.

**Official domain:** 4.

[AWS reference](https://aws.amazon.com/ec2/pricing/)

</details>

---

<!-- question-id: CLF-D4-005; domain: 4; select: 1 -->
## Question 5

What is the best use of AWS Pricing Calculator? Select one answer.

A) Block IAM access

B) Estimate architecture costs before deployment

C) Deploy resources automatically

D) Detect malware

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** IAM policies control access.

- **B — Correct:** Pricing Calculator models estimated costs from configuration and usage assumptions; estimates are not billing guarantees.

- **C — Incorrect:** Deployment requires infrastructure or delivery tools.

- **D — Incorrect:** Malware detection requires security tooling, not a pricing estimator.

**Official domain:** 4.

[AWS reference](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html)

</details>

---

<!-- question-id: CLF-D4-006; domain: 4; select: 1 -->
## Question 6

Which current AWS Support plan is recommended for business-critical workloads and provides designated Technical Account Manager guidance? Select one answer.

A) Basic Support

B) AWS Free Tier

C) Enterprise Support

D) AWS Pricing Calculator

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** C

- **A — Incorrect:** Basic provides account and billing assistance and self-service resources, without designated TAM guidance.

- **B — Incorrect:** Free Tier is an eligibility and usage benefit program, not a support plan.

- **C — Correct:** Enterprise Support provides designated TAM guidance for business-critical workloads; consult the current plan comparison for service terms.

- **D — Incorrect:** Pricing Calculator estimates costs and is not a support plan.

**Official domain:** 4.

[AWS reference](https://aws.amazon.com/premiumsupport/plans/)

</details>

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
