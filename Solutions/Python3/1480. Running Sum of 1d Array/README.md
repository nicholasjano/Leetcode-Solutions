# Solution Walk Through
Question: https://leetcode.com/problems/running-sum-of-1d-array/

## Intuition
For each number, update it to it's current value + the value of the previous number. If done in order, the previous number will be the running sum, so you won't need to use any Auxiliary Space.

## Approach
- Loop from the second item in nums to the end. In each loop, update the value of the current index to current value + the value of the previous number.

## Time Complexity
$O(n)$

$n$ is the length of nums.

## Space Complexity
$O(1)$