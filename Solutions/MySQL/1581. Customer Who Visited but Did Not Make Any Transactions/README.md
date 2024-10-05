# Solution Walk Through
Question: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

## Intuition
I can use a left join to get all the transactions per visit, with null if there are no transactions per visit. I can filter by this null while grouping per customer to get the amount of visits with no transactions.

## Approach
- Select customer_id from visits.
- Included in the select is the count of visit_id, but this will be filtered to only include the visits with no transactions
- A left join is done with the transactions table, and a where clause is used to filter all rows only if the transaction_id is null, meaning a visit with no transaction.
- Group by customer_id to ensure the count of visit_id's is allocated properly to each customer.