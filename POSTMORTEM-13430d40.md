**Incident Postmortem**
=======================

**Incident ID**
---------------

* 13430d40-3e5b-45ce-8ef6-0c8ec58221a7

**Date**
--------

* 2026-05-16

**Summary**
-----------

On 2026-05-16, the target-app service experienced a high error rate on the /checkout endpoint, with a 25% error rate detected in the last 5 minutes. The incident was triggered by a sentinel-ui alert and was subsequently triaged, diagnosed, and resolved.

**Timeline**
------------

* 2026-05-16T03:43:20.530428+00:00: Incident triggered by sentinel-ui alert with a high error rate on the /checkout endpoint.
* 2026-05-16T03:43:20.530428+00:00: Triage completed, incident severity downgraded to P2.
* 2026-05-16T03:43:21.743194+00:00: Diagnostics completed, metrics showed 0 errors and 0 latency.
* 2026-05-16T03:43:21.743194+00:00: Root cause analysis completed, identified a recent commit that introduced a bug in the sentinel logic.
* 2026-05-16T03:43:21.743194+00:00: Fix completed, a PR was created to fix the bug.
* 2026-05-16T03:43:21.743194+00:00: Deployment completed, the fix was rolled out to production.

**Root Cause**
--------------

The root cause of the incident was a recent commit (ad71a642) that introduced a bug in the sentinel logic, specifically the call to `calculate_discount_buggy` for the 'BUGGY' coupon code. This function raises a KeyError if the coupon code is not found, but the 'BUGGY' coupon code is not a valid coupon code.

**Resolution**
--------------

The incident was resolved by creating a PR (207) to fix the bug. The PR removed the call to `calculate_discount_buggy` when the coupon code is 'BUGGY' and instead called the `calculate_discount` function. The fix was rolled out to production using the sentinel deployment process.

**Action Items**
----------------

* Review the recent commits to ensure that similar bugs are not introduced in the future.
* Update the sentinel deployment process to include automated testing for critical functionality.
* Consider implementing a more robust testing framework to catch bugs like this in the future.

**Lessons Learned**
-------------------

* The importance of thorough testing and code review to catch bugs like this before they reach production.
* The value of having a robust incident response process in place to quickly identify and resolve issues.
* The need for continuous improvement and learning from incidents to prevent similar issues in the future.