# Postmortem Report
## Incident ID: edd21216-4fec-479b-ae1d-7a421174c22b

## Date: 2026-05-16

## Summary

On 2026-05-16, a production incident was detected by Datadog's benchmark test, indicating a high error rate in the target-app service. The incident was initially classified as P1 but was later downgraded to P2 due to its non-critical nature. The root cause was identified as a recent commit that reverted a change made in a previous commit, causing a regression. The issue was resolved by reverting the change and deploying a fix.

## Timeline

* 04:02:18 UTC: Incident detected by Datadog's benchmark test
* 04:02:18 UTC: Incident triaged as P2, proceeding autonomously
* 04:10:24 UTC: Diagnostics completed, showing no errors and low latency
* 04:10:24 UTC: Root cause analysis completed, identifying the recent commit as the cause of the issue
* 04:10:24 UTC: Fix deployed to production
* 04:10:24 UTC: Deployment completed successfully

## Root Cause

The root cause of the incident was a recent commit (30262af1) that reverted a change made in a previous commit, causing a regression. The commit removed a call to `calculate_discount()` when the coupon code is 'BUGGY', leading to incorrect discounts being applied.

## Resolution

The issue was resolved by reverting the change made in commit 30262af1 and deploying a fix. The fix added back the call to `calculate_discount()` when the coupon code is 'BUGGY'. The fix was deployed to production, and the incident was closed.

## Action Items

* Review the recent commits to ensure that they are properly tested and do not cause any regressions
* Investigate the code changes made in commit 30262af1 to ensure that they are correct
* Update the documentation to reflect the correct behavior of the `calculate_discount()` function

## Lessons Learned

* The importance of proper testing and review of code changes before deploying them to production
* The need to investigate and understand the root cause of incidents to prevent similar issues from occurring in the future
* The value of having a clear and concise process for resolving incidents and communicating with stakeholders