# Solution Walk Through
Question: https://leetcode.com/problems/combine-two-tables/

## Intuition
Left join the tables, to ensure no person is lost

## Approach
- Select fname and lname from the Person table, and city and state from the Address table
- Select from Person, including a left join with the Address table, ensuring all people are kept