# Solution Walk Through
Question: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

## Intuition
Instead of using a monotonic stack, I can just keep the count of the current increasing/decreasing sequence, as well as the max increasing/decreasing sequence. At the end, I can just return whichever is larger.

## Approach
- Initalize the variables for the current increasing/decreasing sequence, as well as the max increasing/decreasing sequence.
- Loop through `nums`, and check if the adjacent numbers are increasing, decreasing or equal.
- If increasing, add to the current increasing sequence, and check if it's the new max, and set the current decreasing sequence back to 1.
- If decreasing, add to the current decreasing sequence, and check if it's the new max, and set the current increasing sequence back to 1.
- If they are equal, set both the current increasing sequence and current decreasing sequence back to 1.
- Once the loop is complete, return the higher of the max sequences.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$