**Incident Postmortem: 7fb5eea2-37c3-4a0c-a0e4-8f5398b79fff**

**Incident ID:** 7fb5eea2-37c3-4a0c-a0e4-8f5398b79fff
**Date:** 2026-05-16

**Summary**
A high error rate was detected in the target-app service in production, triggering a P1 incident. After triage, the incident was downgraded to P2, and diagnostics were performed. The root cause was identified as a recent commit that removed a call to calculate_discount() when the coupon code is 'BUGGY'. The issue was resolved by reverting the commit and deploying a fix.

**Timeline**
- 04:01:29 UTC: Incident triggered by Datadog due to high error rate in target-app service.
- 04:01:29 UTC: Triage completed, incident downgraded to P2.
- 04:01:30 UTC: Diagnostics completed, logs and metrics analyzed.
- 04:01:30 UTC: Root cause analysis completed, commit 30262af1 identified as the root cause.
- 04:01:30 UTC: Fix prepared and deployed.
- 04:01:30 UTC: Deployment completed, fix rolled out to target-app service.

**Root Cause**
The root cause of the incident was a recent commit (30262af1) that removed the call to calculate_discount() when the coupon code is 'BUGGY'. This commit was reverted by a subsequent commit (af250008), which added back the call to calculate_discount(). However, the original commit was not properly tested, leading to the high error rate.

**Resolution**
The incident was resolved by reverting the commit 30262af1 and deploying a fix that adds back the call to calculate_discount() when the coupon code is 'BUGGY'. The fix was deployed to the target-app service, and the error rate returned to normal.

**Action Items**
- Review the testing process for recent commits to ensure that they are properly tested before deployment.
- Implement additional checks to prevent similar issues in the future.
- Review the commit history to identify any other potential issues.

**Lessons Learned**
- The importance of thorough testing before deployment.
- The need for additional checks to prevent similar issues in the future.
- The value of reviewing the commit history to identify potential issues.

**Recommendations**
- Implement automated testing for recent commits.
- Develop a process for reviewing the commit history to identify potential issues.
- Provide additional training to developers on the importance of thorough testing.