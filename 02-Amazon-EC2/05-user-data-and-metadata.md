# User Data And Metadata

User data and instance metadata help automate and identify EC2 instances, but they serve different purposes.

- **User data:** script provided at launch, used to install and start the application.
- **Metadata:** data queried by the instance, such as IAM role ID, network, and temporary credentials.
- Prefer IAM roles to permanent keys stored in user data.
- **Test tip:** automatic initialization points to user data; data from the instance itself points to metadata.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil


---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
