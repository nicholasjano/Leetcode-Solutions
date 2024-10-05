# Solution Walk Through
Question: https://leetcode.com/problems/invalid-tweets/

## Intuition
Just simply select the ids for all tweets that have a content length greater than 15.

## Approach
- Select tweet_id from tweets
- Use a where clause to filter only tweets where the content is longer than 15 characters long.