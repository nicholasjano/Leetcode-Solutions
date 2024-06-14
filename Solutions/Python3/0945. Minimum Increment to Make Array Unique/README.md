# Solution Walk Through
Question: https://leetcode.com/problems/minimum-increment-to-make-array-unique

## Intuition
Use the counting approach to count how many times each number appears in the list. Handle any duplicates by moving them to the next value.

## Approach
- Account for the base case where nums is empty
- Create a list count with zeroes, of length max(nums) + len(nums)
- For each value in nums, increment that count index by one. This helps us find duplicates.
- Loop through count, and if there are any duplicates, move them to the next index.
- Keep looping until eventually every number is on a unique state


## Time Complexity
$O(n+k)$

$n$ is the length of nums

$k$ is the range from 0 to max(nums) + len(nums)

## Space Complexity
$O(k)$