# Solution Walk Through
Question: https://leetcode.com/problems/find-total-time-spent-by-each-employee/

## Intuition
Since I need to calculate the total time by each employee on each day, I'd need to group by both day and employee. I can just do the sum of out_date - in_time to find the total time.

## Approach
- Select event_day and emp_id from Employees.
- In addition ot the select, add sum(out_time - in_time) to get the sum of all minutes spent in the office.
- Group by event_day and emp_id to ensure the sum calculation only calculates for each (event_day, emp_id) pair.