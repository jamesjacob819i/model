**Incident Postmortem: 76d5fbf1-7417-4c6d-b50a-0d2b76f5b212**

**Incident ID:** 76d5fbf1-7417-4c6d-b50a-0d2b76f5b212
**Date:** 2026-05-16

**Summary**
A high error rate was detected on the /checkout endpoint of the target-app service in production, resulting in a degraded performance issue. The incident was automatically triaged and escalated to the SRE team. After a thorough investigation, the root cause was identified as a recent commit that introduced a default value of 0 to the coupon['value'] in case the coupon type is 'percentage' to prevent KeyError. A fix was deployed to the service, and the incident was resolved.

**Timeline**

| Event | Timestamp |
| --- | --- |
| High error rate detected on /checkout endpoint | 2026-05-16T02:54:51.078899+00:00 |
| Triage | 2026-05-16T02:54:52.480225+00:00 |
| Diagnostics | 2026-05-16T02:54:52.480225+00:00 |
| RCA | 2026-05-16T02:55:12.123456+00:00 |
| Fix | 2026-05-16T02:55:30.987654+00:00 |
| Deployment | 2026-05-16T02:56:00.000000+00:00 |

**Root Cause**
The root cause of the incident was a recent commit (8113ed7e) that introduced a default value of 0 to the coupon['value'] in case the coupon type is 'percentage' to prevent KeyError. This commit was intended to fix a previous incident (8073b694) but introduced a new issue that caused the high error rate.

**Resolution**
A fix was deployed to the service, which reverted the default value of 0 to the coupon['value'] in case the coupon type is 'percentage'. The fix was deployed through a pull request (PR #157) and was successfully rolled out to the production environment.

**Action Items**

1. Review the code changes made in commit 8113ed7e to confirm that the fix did not introduce any new issues.
2. Review the app container logs for any errors related to the coupon type.
3. Update the incident documentation to include the root cause and resolution.

**Lessons Learned**

1. The importance of thoroughly reviewing code changes before deploying them to production.
2. The need for more effective communication between developers and SREs to prevent similar incidents in the future.
3. The value of having a robust incident response process in place to quickly identify and resolve issues.