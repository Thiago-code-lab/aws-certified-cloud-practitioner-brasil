# Static Website

An S3 bucket can host HTML, CSS, JavaScript, and images without running code on the server.

- Configure the index document and error page.
- For HTTPS, a custom domain, and global caching, use CloudFront.
- Prefer private access through CloudFront over direct bucket exposure.
- **Exam tip:** dynamic applications or APIs require additional computation.

Deep dive into AWS architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english



> For additional practice with AWS data projects, explore this course: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## Two distinct hosting patterns

The S3 website endpoint requires public access and supports HTTP only. For a private bucket and HTTPS delivery, use CloudFront OAC with the S3 REST origin, not the website endpoint. Set the CloudFront default root object to `index.html`. AWS also recommends Amplify Hosting for managed static website deployment.

[AWS static hosting guidance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html) · [CloudFront OAC](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

## Official AWS references

- [AWS reference 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [AWS reference 2](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
