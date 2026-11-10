# Lab 01 Initial Iam

This lab practices identities, groups, policies, MFA, and least privilege in AWS IAM.

## Purpose

Create a study user with access to the console through a group, without using the root account for daily tasks.

## Steps

1. Sign in with the root account only to enable MFA and review the account's contacts.
2. In IAM, create an administrative group for the lab and associate the appropriate policy with the study environment.
3. Create a user, add them to the group and enable console access.
4. Log in with the new user and confirm that the expected access works.
5. Review the credentials report and remove credentials that will not be used.

## Check

- The root account has MFA.
- User is granted permissions by group, not by multiple direct policies.
- There are no unnecessary access keys.

## Cleaning

Remove the user and group if the account is no longer used for studies.

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
