# Solution Walk Through
Question: https://leetcode.com/problems/last-person-to-fit-in-the-bus/

## Intuition
Create a CTE to have a column for cumulative weight, and then select the final person before the cumulative weight is over 1000.

## Approach
- Create CTE that adds a column for cumulative weight
- In the main query, select person_name from the CTE
- Add a where clause to filter only people that have a cumulative weight value of 100 or less
- Order in decending order to ensure the final person on the bus is at the top
- Limit by 1 to only return the final person