# Solution Walk Through
Question: https://leetcode.com/problems/not-boring-movies/

## Intuition
Use the modulo operator to determine if an id is odd, then make sure the description is not equal to boring. Afterword, order then in descending order.

## Approach
- Select all columns from table cinema
- Ensure that only odd numbered IDs are being considered with id % 2 = 1
- Ensure only non-boring descriptions are being considered with description != 'boring'
- Order by rating in descending order