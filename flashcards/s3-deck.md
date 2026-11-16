# Deck Amazon S3

<!-- question-id: CLF-FLASH-S3-001; domain: 3; type: open-response -->
## Card 01
**Question:** In S3, what is stored inside a bucket?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Objects. Each object combines data, metadata, and a unique key within the bucket.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-002; domain: 3; type: open-response -->
## Card 02
**Question:** What mental number helps you remember the durability of the S3?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Standard is designed for 99.999999999% annual object durability (eleven nines). Durability describes object preservation and is separate from availability. This is a durability design target for supported S3 storage classes, not a guarantee of continuous availability.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-003; domain: 3; type: open-response -->
## Card 03
**Question:** Versioning best protects against which operational accident?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
Accidentally overwriting or deleting objects. It allows you to recover previous versions when enabled on the bucket.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-004; domain: 3; type: open-response -->
## Card 04
**Question:** When is lifecycle the most likely answer?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
When the statement asks to automatically move objects to cheaper classes or expire old data.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-005; domain: 3; type: open-response -->
## Card 05
**Question:** Which S3 storage class is a straightforward choice for frequently accessed data with predictable access requirements?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Standard. It's the default choice for frequent access, low latency, and high availability.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-006; domain: 3; type: open-response -->
## Card 06
**Question:** For data that is rarely accessed but needs to be returned quickly, which class family makes sense?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Standard-IA or S3 One Zone-IA. The choice depends on the availability requirement and the accepted risk.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-007; domain: 3; type: open-response -->
## Card 07
**Question:** If recovery can take minutes or hours and the goal is cheap archiving, what clue appears?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Glacier Flexible Retrieval offers asynchronous restores measured in minutes to hours depending on tier; S3 Glacier Deep Archive supports longer retrieval times, typically hours. S3 Glacier Instant Retrieval instead provides millisecond access. Select the class by access frequency, retrieval time, and minimum-duration charges.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-008; domain: 3; type: open-response -->
## Card 08
**Question:** Static site on S3 only requires uploading HTML files?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. Direct S3 website hosting requires website configuration and public read permissions and supports HTTP only. The preferred private-bucket pattern uses CloudFront with an S3 REST origin, origin access control (OAC), a scoped bucket policy, and a default root object; it does not require enabling the S3 website endpoint.


[AWS reference](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

</details>

<!-- question-id: CLF-FLASH-S3-009; domain: 3; type: open-response -->
## Card 09
**Question:** Which modern control should be preferred over individual ACLs for bucket access?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
IAM policies and bucket policies. ACLs are less suitable for broad governance in current environments.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-010; domain: 3; type: open-response -->
## Card 10
**Question:** Does S3 serve as the boot disk of an EC2 instance?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
No. S3 is object storage via API. For EC2 block volume, remember Amazon EBS.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-011; domain: 3; type: open-response -->
## Card 11
**Question:** Which feature helps distant users send objects to S3 with less latency impact?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
S3 Transfer Acceleration, using AWS Edge Networking to accelerate transfers in specific scenarios.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

<!-- question-id: CLF-FLASH-S3-012; domain: 3; type: open-response -->
## Card 12
**Question:** S3 Intelligent-Tiering solves what common storage question?

<details>
<summary><strong>View answer</strong></summary>

**Answer:**
When the access pattern is unknown or changes over time. It moves objects between access tiers to automatically optimize cost.


[AWS reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

</details>

---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
