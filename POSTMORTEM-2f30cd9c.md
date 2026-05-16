**Incident Postmortem: 2f30cd9c-105f-4d4f-ac31-77477baf68aa**

**Incident ID:** 2f30cd9c-105f-4d4f-ac31-77477baf68aa
**Date:** 2026-05-16

**Summary**
A high error rate was detected on the /checkout endpoint in the target-app service, with a 25% error rate in the last 5 minutes. The incident was initially marked as P1 but was later downgraded to P2 due to the lack of critical impact. The root cause was identified as a recent commit that changed the logic for handling the 'BUGGY' coupon code, causing a value exception. The incident was resolved by deploying a patch that fixed the issue.

**Timeline**

| Event | Timestamp |
| --- | --- |
| High error rate detected on /checkout endpoint | 2026-05-16T02:01:29.978465+00:00 |
| Triage | 2026-05-16T02:01:30.831679+00:00 |
| Diagnostics | 2026-05-16T02:01:30.831679+00:00 |
| RCA | 2026-05-16T02:01:30.831679+00:00 |
| Fix | 2026-05-16T02:01:30.831679+00:00 |
| Deployment | 2026-05-16T02:01:30.831679+00:00 |

**Root Cause**
The root cause of the incident was a recent commit (e1d6ac4d) that changed the logic for handling the 'BUGGY' coupon code, causing a value exception. This commit was made to fix a previous incident (2343d7ab) and was not thoroughly tested.

**Resolution**
The incident was resolved by deploying a patch that fixed the issue. The patch was created by reverting the changes made in the suspect commit and updating the code to handle the 'BUGGY' coupon code correctly.

**Action Items**

* Review the testing process to prevent similar issues in the future.
* Investigate the code changes in the suspect commit to confirm the root cause.
* Update the documentation to reflect the correct handling of the 'BUGGY' coupon code.

**Lessons Learned**

* The importance of thorough testing and code review before deploying changes to production.
* The need for clear and accurate documentation to prevent similar issues in the future.
* The value of having a robust incident response process in place to quickly identify and resolve issues.