# Cloud Fundamentals Deck

<!-- question-id: CLF-FLASH-CLOUD-001; domain: 1; type: open-response -->
## Card 01
**Question:** If the test mentions "increasing and reducing resources as demand changes", which concept does it want to test?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Elasticity. The memorization signal is dynamic adjustment: resources rise at a peak and fall when demand falls.


[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-002; domain: 1; type: open-response -->
## Card 02
**Question:** Is scalability the same thing as elasticity?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. Scalability is the ability to change capacity to meet requirements; elasticity dynamically matches that capacity to demand, including scaling down.


[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-003; domain: 1; type: open-response -->
## Card 03
**Question:** In a question about low latency for users in a particular geographic area, the first decision usually involves what?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Choice of Region. Region defines geographic proximity, data residency and direct impact on latency.


[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-004; domain: 1; type: open-response -->
## Card 04
**Question:** What does an Availability Zone represent in the global AWS infrastructure?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
One or more isolated data centers within a Region. Different AZs reduce the impact of local failures.


[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

<!-- question-id: CLF-FLASH-CLOUD-005; domain: 1; type: open-response -->
## Card 05
**Question:** When the most likely answer is Multi-AZ, what clue does the statement typically give?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Continuity during a failure affecting an Availability Zone. A multi-zone deployment with failover supports high availability within a Region; it does not protect an on-premises component by itself.


[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

<!-- question-id: CLF-FLASH-CLOUD-006; domain: 1; type: open-response -->
## Card 06
**Question:** What benefit of the cloud exchanges initial hardware investment for operational payment?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Exchange CAPEX for OPEX. Instead of purchasing capacity up front, the company pays for resources as they use them.


[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-007; domain: 1; type: open-response -->
## Card 07
**Question:** "Provision environment in minutes" points to what core advantage of the cloud?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Agility. The cloud reduces infrastructure wait times and speeds up experiments, testing and launches.


[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-008; domain: 1; type: open-response -->
## Card 08
**Question:** In the shared responsibility model, who is responsible for security "of" the cloud and security "in" the cloud?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS secures your cloud infrastructure. The customer protects what they put in the cloud: data, identities, permissions and configurations.


[AWS reference](https://aws.amazon.com/compliance/shared-responsibility-model/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-009; domain: 1; type: open-response -->
## Card 09
**Question:** Are high availability and fault tolerance perfect synonyms?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. High availability seeks to keep the service accessible; Fault tolerance emphasizes continuing to operate even when components fail.


[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

<!-- question-id: CLF-FLASH-CLOUD-010; domain: 1; type: open-response -->
## Card 10
**Question:** What is the idea behind cloud "economies of scale"?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
AWS operates at massive scale and passes cost efficiencies to customers through shared pricing and services.


[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-011; domain: 1; type: open-response -->
## Card 11
**Question:** If the company wants to stop guessing about future capacity, which cloud principle solves it best?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Capacity on demand. The focus is to reduce over-provisioning and under-provisioning, adjusting resources when necessary.


[AWS reference](https://aws.amazon.com/what-is-cloud-computing/)

</details>

<!-- question-id: CLF-FLASH-CLOUD-012; domain: 1; type: open-response -->
## Card 12
**Question:** Test error: choosing Multi-Region whenever "high availability" appears. What is the correct setting?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
For CLF-C02, Multi-AZ is often a sufficient answer for regional high availability. Multi-Region comes in when there is regional disaster, global latency or geographic requirements.


[AWS reference](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
