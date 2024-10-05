# Solution Walk Through
Question: https://leetcode.com/problems/concatenation-of-array/

## Intuition
When creating a count list in python, I can simply do `countList = [0] * n` and it will multiply the list `n` times. Knowing this, the same approach can be applied here, but since we only need to double the list, I can just return `nums * 2`.

## Approach
- Return the concatenated array of `nums * 2`.

## Time Complexity
$O(n)$

$n$ is the length of nums.

## Space Complexity
$O(n)$