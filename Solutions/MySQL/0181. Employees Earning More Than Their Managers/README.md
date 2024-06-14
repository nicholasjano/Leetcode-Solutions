# Solution Walk Through
Question: https://leetcode.com/problems/employees-earning-more-than-their-managers/

## Intuition
Join the Employee table with a copy of itself, but match the managerid with id, so each employee will be in the same row as their manager.

## Approach
- Select employee name from the Employee table
- Select from Employee, including a join with a copy of Employee, matching managerid with id
- Where clause to check if the employee makes more than their manager