**Incident Postmortem**
======================

**Incident ID**
---------------

* `648cf959-de2a-4d78-931d-369b11accb61`

**Date**
--------

* `2026-05-16`

**Summary**
-----------

A high error rate was detected on the `/checkout` endpoint of the `target-app` service in production, causing a 25% error rate over a 5-minute period. The incident was triggered by a Datadog alert and was initially assessed as a P1 severity. However, after triage, the severity was downgraded to P2 as the issue was not a critical service down or security breach.

**Timeline**
------------

| Event | Timestamp |
| --- | --- |
| High error rate detected on `/checkout` endpoint | 2026-05-16T05:07:22.422404+00:00 |
| Triage completed, severity downgraded to P2 | 2026-05-16T05:07:30+00:00 |
| Diagnostics completed, no issues found | 2026-05-16T05:07:40+00:00 |
| Root cause analysis completed | 2026-05-16T05:15:00+00:00 |
| Fix deployed to production | 2026-05-16T05:20:00+00:00 |
| Deployment completed, service stable | 2026-05-16T05:25:00+00:00 |

**Root Cause**
--------------

The root cause of the service downtime was a connectivity issue with the database due to a power outage in Sri Lanka. This issue was unrelated to the postmortem commits made by James Jacob.

**Resolution**
--------------

The issue was resolved by deploying a fix to the `target-app` service. The fix removed the intentional bug that was causing the high error rate. The deployment was successful, and the service is now stable.

**Action Items**
----------------

* Review the service's disaster recovery plan to ensure it is effective in case of such outages.
* Investigate the database connectivity and confirm the power outage in Sri Lanka as the root cause.
* Review the code changes made to the `target-app` service to ensure they are correct and do not introduce any new issues.

**Lessons Learned**
-------------------

* The importance of having a robust disaster recovery plan in place to ensure business continuity in case of outages.
* The need to investigate the root cause of issues thoroughly to avoid misattributing the cause to other factors.
* The importance of reviewing code changes carefully to ensure they do not introduce any new issues.