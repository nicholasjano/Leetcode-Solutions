# Solution Walk Through
Question: https://leetcode.com/problems/reformat-department-table/

## Intuition
I can create 12 new columns, one for each month, where the value in each column is calculated as the sum of revenues for the corresponding (month, id) pair.

## Approach
- Select id from department
- Included in the select, there is an if statement for each month, where the revenue is summed for each (month, id) pair. If not applicable, the result will be null for that cell.
- Group by id to ensure each id has their own row with their own sums in the resulting table.