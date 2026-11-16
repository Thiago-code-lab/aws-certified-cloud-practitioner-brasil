# Lab 03 — Basic CloudWatch Monitoring

Practice metrics, optional dashboards, and alarms. Static documentation review: November 10, 2026. This lab was not executed in AWS.

## Objective

Observe an existing metric and create a monitoring-only alarm. Understand `OK`, `ALARM`, and `INSUFFICIENT_DATA` without generating expensive load or changing the monitored resource.

## Prerequisites and costs

Use an existing authorized lab EC2 instance that already emits metrics. If none exists, stop and read the references; this lab does not require launching infrastructure. Select its Region and record its instance ID. Use a role allowed to read metrics and manage the lab alarm; SNS and dashboard permissions are optional. Review [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) and Free Tier eligibility. Alarms, dashboards, SNS delivery, and the instance may incur charges. Budget alerts are not hard caps.

## Steps

1. Open CloudWatch in the instance's Region. Under Metrics, choose `AWS/EC2`, per-instance metrics, the correct `InstanceId`, and `CPUUtilization`. If no data appears, check the Region, running state, and publication delay.
2. Select Average with a five-minute period, suitable for EC2 basic monitoring. Do not enable paid detailed monitoring. Compare recent values in the graph.
3. Create `CloudPractitionerCpuLab` with a static threshold greater than 80 percent, two of two five-minute datapoints required, and missing-data treatment set to missing. Attach no stop, terminate, reboot, scaling, or other resource-changing actions.
4. Leave notifications disabled unless a dedicated authorized SNS test topic already exists. For email, confirm your own test subscription first. Do not attach an operational team's topic.
5. Observe the alarm after evaluation. A quiet instance may remain `OK`; do not force an alarm. It may initially show `INSUFFICIENT_DATA`. Record the threshold, period, evaluation rule, and observed state.
6. Optionally add the graph to a dedicated lab dashboard after checking pricing. Dashboards visualize metrics; alarms evaluate conditions. Neither replaces CloudTrail's account activity audit.

## Verification

The metric's Region and instance ID match the intended resource. `OK` means the evaluated condition is not breaching; `ALARM` means the configured datapoints meet the breach rule; `INSUFFICIENT_DATA` means there is insufficient information to evaluate. No resource-changing actions are configured. Record SNS delivery as not tested unless it was actually tested with a dedicated subscription. No load generator or detailed monitoring was enabled.

## Cleanup

Delete the alarm and optional dashboard. Remove any SNS resources created specifically for this exercise; preserve pre-existing shared resources. Return the monitored instance to its owner or follow its own authorized cleanup procedure. Confirm that no lab monitoring resources remain and review costs after billing updates.

[AWS CloudWatch overview](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) · [Alarm evaluation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

Architecture: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil/tree/saa-c03-english

AI on AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil
