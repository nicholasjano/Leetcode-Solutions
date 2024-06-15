# Solution Walk Through
Question: https://leetcode.com/problems/search-insert-position/

## Intuition
Use binary search

## Approach
- Implement a binary search algorithm
- Instead of returning -1 if no value is found, return low, which would be the index where it would be if it were inserted in order.

## Time Complexity
$O(\log n)$

## Space Complexity
$O(1)$