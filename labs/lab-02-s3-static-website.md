# Lab 02 Static Site S3

This lab shows how S3 stores objects and can deliver a website consisting of just HTML, CSS, and images.

## Purpose

Create a bucket, submit a simple page, and understand the difference between private access, website endpoint, and secure distribution via CloudFront.

## Steps

1. Create a bucket in a nearby Region and keep public access blocking enabled.
2. Send a file `index.html` without sensitive data.
3. Note that a private object cannot be opened anonymously.
4. For a teaching test, review the static website configuration and required permissions.
5. In a real architecture, prefer CloudFront with private bucket access for HTTPS and cache.

## Check

Confirm that the correct page is returned by the chosen endpoint and that no objects other than those required are exposed.

## Cleaning

Delete the objects, the test distribution if created, and finally the bucket.

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
