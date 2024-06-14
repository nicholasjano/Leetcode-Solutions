# Solution Walk Through
Question: https://leetcode.com/problems/delete-duplicate-emails/

## Intuition
Check for duplicate emails, and delete the one with the largest ID

## Approach
- Delete person from first table
- Use two copies of the table to match emails, and only select to delete the one with the higher ID