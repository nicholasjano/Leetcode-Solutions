# Solution Walk Through
Question: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

## Intuition
Left join the tables to match a unique id for each employee, ensuring no employees are lost.

## Approach
- Select unique employee id from the EmployeeUNI table, as well as their name from the Employees table
- Select from Employees, including a left join with the EmployeeUNI table