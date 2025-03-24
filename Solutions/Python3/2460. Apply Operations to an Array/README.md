# Solution Walk Through
Question: https://leetcode.com/problems/apply-operations-to-an-array/

## Intuition
I can first apply the operations on `nums`, then move all the non-zero numbers to the front of the list, and finally replace the end of the list with zeros.

## Approach
- Loop through `nums` (not including the final index), and complete all the operations if `nums[i] == nums[i + 1]`
- Loop through `nums` and place all the non-zero numbers to the front of the list, keeping a variable to track the current index.
- After all the non-zero numbers are moved to the front of the list, loop from the current index to the end of `nums` and replace the rest of the numbers with zeros to represent all the non-zero numbers.

## Time Complexity
$O(n)$

$n$ is the length of `nums`

## Space Complexity
$O(1)$