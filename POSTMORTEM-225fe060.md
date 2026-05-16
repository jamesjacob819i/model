**Incident Postmortem**
=======================

**Incident ID**
---------------

225fe060-5e8f-4d78-9f36-e7fb889df55f

**Date**
--------

2026-05-16

**Summary**
------------

A high error rate was detected on the `/checkout` endpoint of the `target-app` service in production, with an error rate of 25% in the last 5 minutes. The incident was initially triaged as P1, but was later downgraded to P2 due to the error rate not being critical. The root cause was identified as a recent commit that introduced a bug causing a `KeyError` in the `calculate_discount` function. The issue was resolved by deploying a patch that fixed the bug.

**Timeline**
------------

* 2026-05-16T02:44:46.177941+00:00: High error rate detected on `/checkout` endpoint — 25% error rate in last 5 minutes (sentinel-ui)
* 2026-05-16T02:44:53.522654+00:00: Diagnostics running for service: target-app (diagnostics.done)
* 2026-05-16T02:44:53.522654+00:00: Recent commits show a fix for a `KeyError` issue in the `calculate_discount` function (diagnostics.done)
* 2026-05-16T02:44:53.522654+00:00: Root cause identified as a recent commit that introduced a bug causing a `KeyError` in the `calculate_discount` function (rca.done)
* 2026-05-16T02:44:53.522654+00:00: Patch deployed to fix the bug (fix.done)
* 2026-05-16T02:44:53.522654+00:00: Deployment successful (deployment.done)

**Root Cause**
--------------

The root cause of the incident was a recent commit that introduced a bug causing a `KeyError` in the `calculate_discount` function.

**Resolution**
--------------

The issue was resolved by deploying a patch that fixed the bug. The patch was created by using the `get` method of the dictionary to return a default value (0 in this case) if the key is not present.

**Action Items**
----------------

* Review the recent commits to ensure that the fix is correct and effective.
* Consider implementing additional testing to prevent similar issues in the future.

**Lessons Learned**
------------------

* The importance of thorough testing and review of recent commits to prevent similar issues in the future.
* The value of using the `get` method of the dictionary to return a default value if the key is not present.
* The need for clear and concise communication during incident response to ensure that all stakeholders are informed and aligned.