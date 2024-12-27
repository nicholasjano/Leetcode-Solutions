# Solution Walk Through
Question: https://leetcode.com/problems/product-of-array-except-self/

## Intuition
Loop through `nums`, and keep track of the prefix sum and suffix sum as I go, as the result for a specific index would be the prefix sum times the suffix sum.

## Approach
- Create a result list.
- For each num in `nums`, multiply the cooresponding result list indecies by the prefix and suffix sums respectively.
- Update the prefix and suffix sums.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$