# Lab 01 — Initial IAM Setup

Practice IAM users, groups, policies, MFA, and least privilege. Static documentation review: November 10, 2026. This lab was not executed in AWS.

## Objective

Create a temporary read-only console identity through a group. For ongoing workforce access, prefer federation and temporary credentials through IAM Identity Center. This IAM user exercise demonstrates concepts rather than a recommended workforce architecture.

## Prerequisites and costs

Use an authorized study account without sensitive data. Retain a separate administrator session to avoid locking yourself out. IAM itself has no additional charge; resources you access may incur charges. Review Free Tier eligibility and set a low AWS Budgets alert before other labs. Alerts can be delayed and are not spending caps. Do not create an organization solely for this lab because account-plan eligibility can change.

## Steps

1. If you own the account, use root only to complete required security tasks: enable root MFA and verify recovery contacts. Do not create root access keys or share credentials. Sign out of root. In a managed account, have its administrator verify these controls.
2. Sign in with an authorized administrator role. In IAM, create the group `CloudPractitionerReadOnlyLab` and attach the AWS managed `ReadOnlyAccess` policy. This policy provides broad read access and may expose sensitive data; it is only for this temporary study exercise, not a final least-privilege design.
3. Create the temporary IAM user `cloud-practitioner-reader`, enable console access, require a password change at next sign-in, and add it to the group. Create no access keys. Never commit passwords or enrollment material.
4. Sign in with this user in a separate browser profile, change the temporary password, and open a read-only console page such as the EC2 instance list. The user should not have permission to create or modify resources.
5. For optional study-user MFA practice, use the administrator session to configure its device or supply narrowly scoped self-service permissions. `ReadOnlyAccess` alone does not authorize MFA enrollment. Keep recovery and enrollment secrets private.
6. Return to the administrator session and generate the IAM credential report. Verify that the user has no access keys; inspect password and MFA status. Identify how broad read access could be replaced with actions and resources actually needed for a real role.

## Verification

Root MFA is enabled. The user inherits read permissions from the group and has no access keys. Read-only access works, while write permissions are not granted. IAM is global within an AWS partition: identity configuration is not repeated per Region. Explain that users and roles are persistent IAM identities, while assuming a role provides temporary credentials.

## Cleanup

From the retained administrator session, remove the temporary user's console password, MFA association if configured, group membership, and other credentials or policies. Delete the user. Detach the group policy and delete the empty group. Keep the account owner's root MFA enabled. Verify that no temporary user or access key remains.

[AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) · [Credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english

AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil
