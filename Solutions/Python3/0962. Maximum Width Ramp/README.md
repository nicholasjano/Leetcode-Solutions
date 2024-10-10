# Solution Walk Through
Question: https://leetcode.com/problems/maximum-width-ramp/

## Intuition
I first came up with a brute force solution, where I compared each index with every other index to find the max width. This was not the best solution, so I came up with a method that uses a decreasing monotonic stack. I can use that stack to hold the values that could possibly be the left bound of the max width, and then I can loop once more to find the right bound.

## Approach
- Create a decreasing monotonic stack from `nums`.
- Loop through `nums` backwards, attempting to find a value that is greater than or equal to the most recent value in the stack. If the condition is met, that pair is a potential candidate for the max width, and store it if needed. Pop the stack value as it has already found the best pair candidate for the max width.
- Once either the stack is complete or the loop is complete, return the highest potential candidate for the max width.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$