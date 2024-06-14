# Solution Walk Through
Question: https://leetcode.com/problems/sort-colors/

## Intuition
Since we know the range of nums is 2, we can use a count array with effectively O(1) time.

## Approach
- Place the occurences of each number in count array
- Loop through each index in count array, from index 0 to 2, and loop through their values, adding the index to nums for all occurences

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$