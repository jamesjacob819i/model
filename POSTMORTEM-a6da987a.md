**Incident Postmortem: a6da987a-6172-423e-b5cb-fccf8926eeb7**

**Incident ID:** a6da987a-6172-423e-b5cb-fccf8926eeb7
**Date:** 2026-05-16

**Summary**
A high error rate was detected on the /checkout endpoint of the target-app service in production. The error rate was 25% in the last 5 minutes, but was determined to be non-critical and not require immediate action. After further investigation, a recent commit was identified as the root cause of the issue. The commit introduced a bug in the calculate_discount function, which raised a KeyError when encountering a coupon code that was not in the valid_coupons dictionary. The bug was fixed by changing the function to use the get method instead of direct dictionary access.

**Timeline**

* 2026-05-16T02:28:43.748740+00:00: High error rate detected on /checkout endpoint — 25% error rate in last 5 minutes
* 2026-05-16T02:28:44.578934+00:00: Diagnostics running for service: target-app
* 2026-05-16T02:28:44.578934+00:00: Recent commits indicate that a bug was introduced in the calculate_discount function
* 2026-05-16T02:28:44.578934+00:00: Root cause identified as a recent commit that introduced a bug in the calculate_discount function
* 2026-05-16T02:28:44.578934+00:00: Fix created and deployed to production
* 2026-05-16T02:28:44.578934+00:00: Fix verified to have resolved the issue

**Root Cause**
The root cause of the incident was a recent commit that introduced a bug in the calculate_discount function. The bug was caused by the function raising a KeyError when encountering a coupon code that was not in the valid_coupons dictionary. The commit that introduced the bug was e6a70770.

**Resolution**
The bug was fixed by changing the calculate_discount function to use the get method instead of direct dictionary access. The fix was deployed to production and verified to have resolved the issue.

**Action Items**

* Review the code changes made in the recent commits to ensure that they do not introduce any new bugs.
* Consider implementing additional testing to ensure that the calculate_discount function is working correctly.
* Review the incident response process to ensure that it is effective and efficient.

**Lessons Learned**

* The importance of thorough testing and code review to prevent bugs from being introduced into production.
* The need for clear and effective communication during incident response to ensure that all stakeholders are informed and aligned.
* The value of having a well-defined incident response process in place to ensure that incidents are handled efficiently and effectively.