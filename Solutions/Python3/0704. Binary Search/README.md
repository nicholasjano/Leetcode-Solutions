# Solution Walk Through
Question: https://leetcode.com/problems/binary-search/

## Intuition
Instead of searching through the list one at a time, we can continually search the middle, halving the search area with each search. This will make search go from O(n) to O(logn)

## Approach
- Designate the low and high values to cover the full list.
- In a while loop, generate the mid value.
- If the target is greater than the mid value, move the low value one above the middle value, and enter the loop again.
- If the target is less than the mid value, move the high value and below the middle value, and enter the loop again.
- Keep looping until either the target is found, or low becomes greater than high.

## Time Complexity
$O(\log n)$

## Space Complexity
$O(1)$