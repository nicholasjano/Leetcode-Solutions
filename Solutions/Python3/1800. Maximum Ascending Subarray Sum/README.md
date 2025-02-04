# Solution Walk Through
Question: https://leetcode.com/problems/maximum-ascending-subarray-sum/

## Intuition
I can loop through `nums`, keeping track of the prefix sum as I go. Once I reach an index where the list is not increasing, I can reset the prefix sum. While I'm doing this, I keep track of the maximum value the prefix sum reaches to be returned at the end.

## Approach
- Initalize the maxmium value and current prefix sum to be the first index of `nums`
- Loop from the second index, and check if the current index value is increasing from the previous index value
- If it is increasing, add the current index value to the prefix sum, and check if a new max has been reached
- If it is not increasing, reset the prefix sum to the current index value
- Once all numbers have been looped though, return the maximum value


## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$