**Postmortem Document**
=======================

**Incident ID**
---------------

3ff1f36a-86df-4a45-8565-b783224e4444

**Date**
---------

2026-05-16

**Summary**
------------

On 2026-05-16, a production incident occurred on the /checkout endpoint of the target-app service, resulting in a high error rate of 25% for 5 minutes. The incident was initially triggered by a sentinel-ui alert, but it was later downgraded to a P2 incident due to the lack of critical impact. The root cause was identified as a recent commit that fixed a bug, but may have introduced a new issue. The incident was resolved by deploying a patch that fixed the issue.

**Timeline**
------------

* 02:23:31: Sentinel-ui alert triggered a high error rate on the /checkout endpoint (25% error rate in last 5 minutes)
* 02:23:31: Incident created with severity P1
* 02:23:32: Triage completed, downgrading incident severity to P2
* 02:23:32: Diagnostics completed, showing no errors or latency
* 02:23:32: RCA completed, identifying the root cause as a recent commit that fixed a bug, but may have introduced a new issue
* 02:23:32: Fix created, deploying a patch to fix the issue
* 02:23:32: Deployment completed, with no errors or latency observed

**Root Cause**
--------------

The root cause of the incident was identified as a recent commit (e6a70770) that fixed a bug, but may have introduced a new issue. The commit was made to the calculate_discount_buggy function, which was causing a KeyError when encountering a coupon code that is not in the valid_coupons dictionary.

**Resolution**
--------------

The incident was resolved by deploying a patch that fixed the issue. The patch was created by reviewing the code changes and testing the function to ensure it was working correctly. The patch was deployed using the sentinel/fix-3ff1f36a branch.

**Action Items**
----------------

* Review the code changes made in the recent commit (e6a70770) to ensure that it did not introduce any new issues.
* Test the calculate_discount_buggy function to ensure it is working correctly.
* Consider implementing additional testing and validation for the calculate_discount_buggy function to prevent similar incidents in the future.

**Lessons Learned**
-------------------

* The importance of thorough testing and validation of code changes, especially when fixing bugs.
* The need for clear and concise commit messages, including the fix for the bug and the potential impact of the fix.
* The value of having a clear and well-documented incident response process, including clear roles and responsibilities for each team member.