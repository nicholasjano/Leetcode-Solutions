# Solution Walk Through
Question: https://leetcode.com/problems/duplicate-emails/

## Intuition
Group by email and check the amount of occurences.

## Approach
- Select email from Person table.
- Group by email, so we can use "having" to check the count of each email
- Only select emails with a count above 1, which are the duplicates