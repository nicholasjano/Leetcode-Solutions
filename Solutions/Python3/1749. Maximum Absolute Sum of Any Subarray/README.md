# Solution Walk Through
Question: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

## Intuition
The sum of a subarray is the difference between two prefix sums. To find the maximum value, I need to find the maximum difference between any two prefix sums.

## Approach
- Initialize variables for the min prefix sum, max prefix sum, and running prefix sum
- Loop through each number in `nums`. Increment the prefix sum by the number.
- Determine if this prefix sum in a new max or min prefix sum, and save if it is.
- Once the loop is done, return the maximum prefix sum - the minimum prefix sum for the maximum absolute subarray sum.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$