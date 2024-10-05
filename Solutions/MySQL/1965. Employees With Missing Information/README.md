# Solution Walk Through
Question: https://leetcode.com/problems/employees-with-missing-information/

## Intuition
Since I'd need to check both if the employee's name is missing, or the employee's salary is missing, I'd need to have a seperate select for each, and union the results. I can utilize joins to be able to filter for each condition.

## Approach
- First select: Select employee_id from employees.
- Left join employees with salaries, ensuring all employees are kept.
- Filter to check if the employee's salary is missing (null).
- Second select: Select employee_id from salaries.
- Right join employees with salaries, ensuring all salaries are kept.
- Filter to check if the employee's name is missing (null).
- Union the two results, and order this all by employee_id ascending.