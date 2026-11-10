# Deck Amazon S3

## Card 01
**Question:** In S3, what is stored inside a bucket?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Objects. Each object combines data, metadata, and a unique key within the bucket.

</details>

## Card 02
**Question:** What mental number helps you remember the durability of the S3?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Eleven nines of durability: 99.999999999%. The proof uses this to enforce preservation of objects, not total absence of unavailability.

</details>

## Card 03
**Question:** Versioning best protects against which operational accident?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Accidentally overwriting or deleting objects. It allows you to recover previous versions when enabled on the bucket.

</details>

## Card 04
**Question:** When is lifecycle the most likely answer?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
When the statement asks to automatically move objects to cheaper classes or expire old data.

</details>

## Card 05
**Question:** Frequently accessed data without a clear pattern should start in which class?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Standard. It's the default choice for frequent access, low latency, and high availability.

</details>

## Card 06
**Question:** For data that is rarely accessed but needs to be returned quickly, which class family makes sense?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Standard-IA or S3 One Zone-IA. The choice depends on the availability requirement and the accepted risk.

</details>

## Card 07
**Question:** If recovery can take minutes or hours and the goal is cheap archiving, what clue appears?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Glacier. For very long retention and very rare access, the evidence may point to Glacier Deep Archive.

</details>

## Card 08
**Question:** Static site on S3 only requires uploading HTML files?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. You need to enable static website hosting, configure index/error document and adjust public reading or distribution via CloudFront.

</details>

## Card 09
**Question:** Which modern control should be preferred over individual ACLs for bucket access?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
IAM policies and bucket policies. ACLs are less suitable for broad governance in current environments.

</details>

## Card 10
**Question:** Does S3 serve as the boot disk of an EC2 instance?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. S3 is object storage via API. For EC2 block volume, remember Amazon EBS.

</details>

## Card 11
**Question:** Which feature helps distant users send objects to S3 with less latency impact?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Transfer Acceleration, using AWS Edge Networking to accelerate transfers in specific scenarios.

</details>

## Card 12
**Question:** S3 Intelligent-Tiering solves what common storage question?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
When the access pattern is unknown or changes over time. It moves objects between access tiers to automatically optimize cost.

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
