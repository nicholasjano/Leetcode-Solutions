# Solution Walk Through
Question: https://leetcode.com/problems/find-followers-count/

## Intuition
Each row is a new follower, so if you just count the occurence of each user_id, that will give you the amount of followers they have.

## Approach
- Select user_id and count(user_id) as followers_count from followers. As mentioned above, just counting the user_id amount for each user will give you the amount of followers they have.
- Group by user_id to ensure each user counts their own followers.
- Order by user_id in ascending order.