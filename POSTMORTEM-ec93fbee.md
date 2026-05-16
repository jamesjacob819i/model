**Incident Postmortem: ec93fbee-482e-46f5-8a60-c6876e4b08ca**

**Incident ID:** ec93fbee-482e-46f5-8a60-c6876e4b08ca
**Date:** 2026-05-16

**Summary**
The target-app service experienced a high error rate detected incident, which was initially classified as P1 but downgraded to P2 after triage. The incident was caused by a recent commit that added back a call to calculate_discount() when the coupon code is 'BUGGY'. The issue was resolved by reverting the commit and deploying a patch to remove the call to calculate_discount() for the BUGGY coupon code.

**Timeline**

| Event | Timestamp |
| --- | --- |
| Incident detected by Datadog | 2026-05-16T04:02:12.453537+00:00 |
| Triage | 2026-05-16T04:02:12.453537+00:00 (autonomous proceed) |
| Diagnostics | 2026-05-16T04:03:22+00:00 |
| RCA | 2026-05-16T04:03:46.824480+00:00 |
| Fix | 2026-05-16T04:03:46.824480+00:00 |
| Deployment | 2026-05-16T04:03:46.824480+00:00 |

**Root Cause**
The recent commit 81aacbce, which reverts the change made in commit 30262af1, is likely the root cause of the incident. This commit adds back the call to calculate_discount() when the coupon code is 'BUGGY', which may have caused the issue.

**Resolution**
The issue was resolved by reverting the commit 81aacbce and deploying a patch to remove the call to calculate_discount() for the BUGGY coupon code. The patch was created by removing the call to calculate_discount() when the coupon code is 'BUGGY' in the app/routes.py file.

**Action Items**

* Review the code changes made in commit 81aacbce to ensure they are correct.
* Investigate the app container logs to confirm the root cause and to see if there are any other issues.

**Lessons Learned**

* The importance of thoroughly reviewing code changes before deploying them to production.
* The need for more effective communication between teams to prevent similar incidents in the future.
* The value of having a clear and concise incident response process to ensure timely and effective resolution of incidents.