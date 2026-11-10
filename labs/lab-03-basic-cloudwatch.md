# Lab 03 Cloudwatch Basic

This lab practices metrics, dashboards, and alarms in Amazon CloudWatch.

## Purpose

View a metric for an existing resource and create a low-risk alarm to understand the monitoring flow.

## Steps

1. Open CloudWatch and find metrics for a lab resource, such as an EC2 instance.
2. Select a metric, adjust the period, and compare the values ​​on the chart.
3. Create an alarm with a simple limit and few evaluations.
4. Configure a notification only if there is a confirmed test SNS topic.
5. Record what the state `OK`, `ALARM`, and `INSUFFICIENT_DATA` represents.

## Check

The alarm must reflect the chosen metric. Don't force expensive load just to change its state.

## Cleaning

Delete the alarm, optional dashboard, and resources used in the test.

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Follow CloudStudy

CloudStudy is available to help learners study AWS. Explore the platform at https://app.cloudstudy.com.br/. These open-source GitHub study materials are free; platform features may have separate terms.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
