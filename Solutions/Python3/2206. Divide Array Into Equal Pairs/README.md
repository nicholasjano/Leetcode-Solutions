# Solution Walk Through
Question: https://leetcode.com/problems/divide-array-into-equal-pairs/

## Intuition
I can use a set to keep track of visited numbers. If a number is already visited, that means a pair is made and it can be removed from the set. If the set is empty after iterating thought `nums`, then the array can be divided into equal pairs.

## Approach
- Create a set to store values from `nums`.
- Iterate through `nums`, if the current number is not in the set, add it, otherwise, remove the number from the set.
- By the end, if the set is empty, return true as the array has been divided into equal parts. Otherwise return false.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$