# Solution Walk Through
Question: https://leetcode.com/problems/the-latest-login-in-2020/

## Intuition
I can use the max function to get the latest login time, and include a filter where only timestampes within 2020 are considered.

## Approach
- Select user_id and max(time_stamp) from logins.
- Use a where clause to only filter by dates in 2020.
- Group by user_id to ensure the resulting table shows the latest login for each user.