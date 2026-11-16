# Domain 1 Questions

6 questions in their original source order. Each question has one correct answer and four alternatives.


---

<!-- question-id: CLF-D1-001; domain: 1; select: 1 -->
## Question 1

A company wants to replace upfront server purchases with monthly usage-based charges. Which option best matches this goal? Select one answer.

A) Guaranteed high latency

B) Elasticity with pay-as-you-go pricing

C) Manual hardware management

D) A fixed five-year contract

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** High latency is a disadvantage, not a cloud benefit.

- **B — Correct:** Usage-based pricing replaces upfront infrastructure purchases; elasticity also supports matching capacity to demand.

- **C — Incorrect:** Managing physical hardware does not provide usage-based cloud billing.

- **D — Incorrect:** A long fixed contract is not required for pay-as-you-go resources.

**Official domain:** 1.

[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

---

<!-- question-id: CLF-D1-002; domain: 3; select: 1 -->
## Question 2

Which statement correctly describes an AWS Region? Select one answer.

A) A single data center

B) A group of Availability Zones in a geographic area

C) A global service with no geographic location

D) A customer-owned private network

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** A Region contains multiple Availability Zones, each with one or more data centers.

- **B — Correct:** A Region is a geographic area with multiple isolated Availability Zones.

- **C — Incorrect:** A Region has a geographic location.

- **D — Incorrect:** A customer network is not an AWS Region.

**Official domain:** 3.

[AWS reference](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html)

</details>

---

<!-- question-id: CLF-D1-003; domain: 1; select: 1 -->
## Question 3

A startup needs to launch a prototype quickly with minimal upfront investment. Which cloud characteristic helps most? Select one answer.

A) High capital expenditure

B) Slow provisioning

C) Provisioning agility

D) Blocked scalability

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** C

- **A — Incorrect:** High upfront capital spending conflicts with the requirement.

- **B — Incorrect:** Slow provisioning delays the prototype.

- **C — Correct:** On-demand provisioning reduces setup time and initial infrastructure investment.

- **D — Incorrect:** Preventing scaling does not help launch or grow a prototype.

**Official domain:** 1.

[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

---

<!-- question-id: CLF-D1-004; domain: 1; select: 1 -->
## Question 4

Which service model provides virtual infrastructure such as instances and basic networking? Select one answer.

A) SaaS

B) PaaS

C) IaaS

D) DaaS

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** C

- **A — Incorrect:** SaaS provides a ready-to-use application.

- **B — Incorrect:** PaaS provides a managed application platform rather than primarily raw infrastructure.

- **C — Correct:** Infrastructure as a Service provides compute, storage, and networking resources.

- **D — Incorrect:** Desktop as a Service provides virtual desktops rather than the general infrastructure model described.

**Official domain:** 1.

[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

---

<!-- question-id: CLF-D1-005; domain: 1; select: 1 -->
## Question 5

Which approach usually improves an application's availability within an AWS Region? Select one answer.

A) Use a single Availability Zone

B) Distribute the application across multiple Availability Zones

C) Keep only a local backup

D) Increase disk capacity

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** A single-zone deployment remains exposed to that zone becoming unavailable.

- **B — Correct:** Independent zones reduce the impact of a failure affecting one location when the application is designed for failover.

- **C — Incorrect:** A backup supports recovery but does not keep the application serving traffic during a failure.

- **D — Incorrect:** A larger disk alone does not add redundant application locations.

**Official domain:** 1.

[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

---

<!-- question-id: CLF-D1-006; domain: 1; select: 1 -->
## Question 6

Which option best represents scalability? Select one answer.

A) Keep capacity fixed

B) Adjust resource capacity to meet workload requirements

C) Buy spare servers once per year

D) Remove monitoring

<details>
<summary><strong>View answer and explanations</strong></summary>

**Correct answer:** B

- **A — Incorrect:** Fixed capacity cannot accommodate changing capacity requirements.

- **B — Correct:** Scalability is the ability to change capacity; elasticity emphasizes dynamically matching capacity to demand.

- **C — Incorrect:** Annual purchases alone do not demonstrate the ability to adjust capacity as required.

- **D — Incorrect:** Removing monitoring does not increase capacity and reduces visibility.

**Official domain:** 1.

[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/
