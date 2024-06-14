# Solution Walk Through
Question: https://leetcode.com/problems/employee-bonus/

## Intuition
Join the tables, and use a where statement to check if the bonus is under 1000

## Approach
- Select employee name from the employee table, as well as their bonus
- Select from employee, including a left join with the bonus table, ensuring all employees are kept
- If the employee either doesn't have a bonus (null) or has a bonus value under 1000, select them.