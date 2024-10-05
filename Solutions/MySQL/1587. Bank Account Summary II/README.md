# Solution Walk Through
Question: https://leetcode.com/problems/bank-account-summary-ii/

## Intuition
I definitely need to use a join to get the transactions per user. Afterward, I can sum the transactions to get thier balance, filtering by only 10,000+. 

## Approach
- Select name from users.
- Included in the select is the sum of transaction amounts from the transactions table.
- An inner join is done with the transactions table to ensure the transaction amounts can be selected and aggregated.
- Group by account to ensure the sum of amounts is allocated properly to each user.
- Utilize a having clause to filter for only transaction amounts of 10,000+.