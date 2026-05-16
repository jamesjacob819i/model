**Incident Postmortem**
======================

**Incident ID**
---------------

8ab0d716-5d26-4e60-ba24-d9dc8e027614

**Date**
--------

2026-05-16

**Summary**
------------

A high error rate was detected in the target-app service in production. The incident was initially triaged as P1, but upon further investigation, it was downgraded to P2. The root cause was identified as a recent commit that removed a call to calculate_discount() when the coupon code is 'BUGGY'. The issue was resolved by reverting the commit and deploying a patch to restore the missing call.

**Timeline**
------------

* 04:02:06 - Incident created due to high error rate detected in Datadog
* 04:02:06 - Triage completed, incident downgraded to P2
* 04:02:30 - Diagnostics completed, logs and metrics analyzed
* 04:02:30 - Root cause analysis completed, suspect commit identified
* 04:02:30 - Fix created, patch deployed to restore missing call
* 04:02:30 - Deployment completed, metrics monitored for stability
* 04:02:30 - Incident closed

**Root Cause**
--------------

The recent commit 30262af1 removed the call to calculate_discount() when the coupon code is 'BUGGY', which was reverted by the subsequent commit af250008. This change caused the high error rate detected in the target-app service.

**Resolution**
--------------

The issue was resolved by reverting the commit 30262af1 and deploying a patch to restore the missing call to calculate_discount() when the coupon code is 'BUGGY'. The patch was created and deployed using the Sentinel tool, and metrics were monitored for stability.

**Action Items**
----------------

* Review the commit history to ensure that similar issues do not occur in the future
* Update the documentation to reflect the correct behavior of the calculate_discount() function
* Consider implementing automated testing to catch similar issues earlier

**Lessons Learned**
-------------------

* The importance of thorough triage and root cause analysis in resolving incidents quickly and effectively
* The value of having a clear and concise documentation of the system's behavior and functionality
* The need for continuous monitoring and improvement of the system to prevent similar issues from occurring in the future