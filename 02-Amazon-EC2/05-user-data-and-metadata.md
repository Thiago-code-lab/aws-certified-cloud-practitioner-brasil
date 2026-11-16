# EC2 User Data and Instance Metadata

EC2 user data and instance metadata help automate and identify instances, but serve different purposes.

- **User data:** a script provided at launch to install software or start an application.
- **Instance metadata:** information retrieved from within the instance, such as ID, network settings, and temporary IAM role credentials.
- Prefer IAM roles over permanent access keys stored in user data.
- **Exam tip:** automatic setup points to user data; information about the running instance points to metadata.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english


---

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
