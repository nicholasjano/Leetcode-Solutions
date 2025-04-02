# Solution Walk Through
Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Intuition
I can use a two pointer approach. The left pointer will be the index where the next unique number goes, and the right pointer finds the next unique number.

## Approach
- Loop through `nums` until a unique number is found. Once found, place that value on the left pointer for the next unique value, and move the left pointer forward by 1.
- Return the left pointer as it represents the total amount of unique numbers.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$