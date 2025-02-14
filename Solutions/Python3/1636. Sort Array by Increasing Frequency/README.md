# Solution Walk Through
Question: https://leetcode.com/problems/sort-array-by-increasing-frequency/

## Intuition
I can get the count of each number using a Counter hashmap, and I can create a custom sort function that sorts by the count. If two numbers have the same count, tiebreak the sort in decreasing order.

## Approach
- Create a counter to store the count of all the numbers from `nums`.
- Create a custom sort where the sorting key is firstly the count, and if there are equal counts, then `-num` to ensure decreasing order.

## Time Complexity
$O(n \log n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$