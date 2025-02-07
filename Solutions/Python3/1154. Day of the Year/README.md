# Solution Walk Through
Question: https://leetcode.com/problems/day-of-the-year/

## Intuition
I can parse the year, month, and day from the string. With the knowledge of the amount of days in each month of the year, I can add all the days of the past months, and then add the day. I'd also need to properly track the leap year.

## Approach
- Parse the Year, Month, and Day from `date`
- Create a list to store the amount of days in each month, and account for the leap year
- Return the sum of days in all the past months, as well as the day

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$