# Solution Walk Through
Question: https://leetcode.com/problems/rising-temperature/

## Intuition
Match reconds with the recond of the previosu day, and check if the temp is higher.

## Approach
- Select the id from the first copy
- Inner join with the second copy, and match the date with the previous date
- Only account for values where the second day has a higher temperature