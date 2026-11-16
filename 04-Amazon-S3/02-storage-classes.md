# Storage Classes

S3 storage classes balance cost, availability, and retrieval time according to the access pattern.

- **Standard:** frequent access.
- **Intelligent-Tiering:** unknown or variable access.
- **Standard-IA/One Zone-IA:** infrequent access with millisecond retrieval and retrieval charges; One Zone-IA stores data in a single AZ and is suitable for reproducible data or secondary backups.
- **S3 Express One Zone:** latency-sensitive, frequently accessed data in a single AZ.
- **Glacier Instant Retrieval:** rarely accessed archive data that still needs millisecond access.
- **Glacier Flexible Retrieval:** archive data restored asynchronously in minutes to hours, depending on the retrieval tier.
- **Glacier Deep Archive:** very infrequently accessed data with retrieval measured in hours.
- **Cost considerations:** IA classes have a 30-day minimum storage duration; Glacier Instant Retrieval and Flexible Retrieval have 90-day minimums, and Deep Archive has a 180-day minimum. Requests, retrievals, and early deletion can add charges. Intelligent-Tiering has monitoring charges for eligible objects; optional archive tiers require restoration.
- **Exam tip:** consider access frequency, resilience across AZs, and retrieval speed.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


---

## Official AWS references

- [Glacier retrieval and minimum storage durations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/glacier-storage-classes.html)

- [AWS reference 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [AWS reference 2](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
