# Lab 02 — Static Website with S3 and CloudFront

Practice object storage, private access, and secure static content delivery. Static documentation review: November 10, 2026. This lab was not executed in AWS.

## Objective

Serve a page over HTTPS through CloudFront with a private S3 REST origin and origin access control (OAC). Compare this with the separate S3 website endpoint without making the bucket public.

## Prerequisites and costs

Use an authorized study role allowed to manage the lab bucket, distribution, and OAC. Choose and record an enabled AWS Region near you. Review [S3 pricing](https://aws.amazon.com/s3/pricing/), [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/), and [Free Tier eligibility](https://aws.amazon.com/free/). Storage, requests, and transfer can be billed. Set a low budget alert; it is not a spending cap. Avoid optional custom domains, logging destinations, and paid features.

## Steps

1. Create a general purpose S3 bucket with a unique name in the selected Region. Keep **Block all public access** enabled and **Bucket owner enforced** Object Ownership. Use default S3-managed encryption for this lab to avoid additional KMS policy configuration. Leave versioning disabled for simpler cleanup.
2. Save the complete page below as `index.html` and upload it. Use no personal data or credentials.

```html
<!doctype html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cloud Practitioner Lab</title>
</head>
<body>
  <h1>Private origin, public HTTPS delivery</h1>
  <p>This page is stored in Amazon S3 and delivered through Amazon CloudFront.</p>
</body>
</html>
```

3. Try the object's ordinary S3 URL in a signed-out browser. Anonymous access should fail. Authenticated console previews and presigned URLs use different access mechanisms.
4. Create a CloudFront distribution using the bucket's **S3 REST origin**, not its website endpoint. Create and attach an OAC with request signing enabled. Set the default root object to `index.html` and redirect HTTP viewers to HTTPS. Use the default CloudFront domain and certificate.
5. Apply the bucket policy generated for this distribution. Verify that it grants the CloudFront service principal only `s3:GetObject` on this bucket's objects and restricts access to the exact distribution `AWS:SourceArn`. Do not add public principals or disable Block Public Access. Wait for distribution deployment to complete.
6. Open the distribution's HTTPS domain. If access fails, check the origin type, OAC, policy distribution ARN, object key, and default root object. Cached errors may take time to expire; avoid repeated invalidations.
7. Inspect S3 static website hosting under bucket Properties without enabling it. The direct website endpoint requires public read access and supports HTTP only. OAC requires an S3 REST origin and cannot secure a website endpoint. AWS also recommends Amplify Hosting for managed static deployment.

## Verification

CloudFront serves the expected page over HTTPS. Anonymous S3 object access stays denied, Block Public Access stays enabled, and the bucket policy is scoped to the distribution. S3 website hosting is not enabled. The public page contains no sensitive information.

## Cleanup

Disable the CloudFront distribution and wait for deployment; then delete it before deleting its OAC-protected bucket. Remove the bucket policy statement for the deleted distribution and delete the unused OAC. Delete all objects, versions and delete markers if versioning was enabled, and incomplete multipart uploads. Delete the empty bucket. Confirm that no distribution, OAC, optional log destination, or other lab resource remains. Review costs again after billing data updates.

[AWS static hosting guidance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html) · [OAC configuration and deletion order](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english

AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil
