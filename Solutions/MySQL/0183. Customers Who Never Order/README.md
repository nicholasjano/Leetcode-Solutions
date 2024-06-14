# Solution Walk Through
Question: https://leetcode.com/problems/customers-who-never-order/

## Intuition
Left join the tables to match a order ids to customer ids, and check if a customer has no matching order
## Approach
- Select customer name from Customers
- Left join with orders, ensuring no customer is lost
- Only select customers with no matching order