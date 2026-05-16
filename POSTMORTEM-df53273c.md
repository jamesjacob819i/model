**Incident Postmortem: df53273c-1398-41cf-9b83-d254e8a269b6**

**Incident ID**
df53273c-1398-41cf-9b83-d254e8a269b6

**Date**
2026-05-16

**Summary**
A high error rate was detected in the target-app service in production, causing a P2 incident. The error was caused by a recent commit that reverted a change that removed a call to calculate_discount() when the coupon code is 'BUGGY'. The incident was resolved by deploying a patch that restored the original behavior.

**Timeline**

* 04:02:10 - Incident detected by Datadog with a P1 severity
* 04:02:10 - Triage completed, severity downgraded to P2
* 04:03:40 - Diagnostics completed, logs and metrics analyzed
* 04:03:40 - Root cause analysis completed, commit 81aacbce identified as the cause
* 04:04:00 - Fix deployed, patch merged and deployed to production
* 04:05:00 - Deployment completed, metrics show improvement

**Root Cause**
The recent commit 81aacbce reverted a change that removed a call to calculate_discount() when the coupon code is 'BUGGY', which is likely the cause of the error. This change was made in a previous commit (30262af1) and was intended to fix a regression.

**Resolution**
A patch was deployed to restore the original behavior by adding back the call to calculate_discount() when the coupon code is 'BUGGY'. The patch was merged and deployed to production, and metrics show improvement.

**Action Items**

* Review the commit history to ensure that similar changes are not made in the future
* Consider implementing automated testing to catch regressions like this one
* Review the deployment process to ensure that changes are properly reviewed and tested before being deployed to production

**Lessons Learned**

* The importance of thorough testing and review of changes before deploying to production
* The need for automated testing to catch regressions like this one
* The value of having a clear and well-documented commit history to aid in root cause analysis