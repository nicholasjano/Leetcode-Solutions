# Solution Walk Through
Question: https://leetcode.com/problems/construct-smallest-number-from-di-string/

## Intuition
I can loop through numbers from 1 to `len(pattern) + 1` (max 9), add the number to the stack, and if the number is increasing, extend the result with the stack, if it is decreasing, just pass. Also, if the pattern has ended, extend the result with the stack. This ensures that the decreasing numbers will be properly reversed because of the stack.

## Approach
- Initialize a result list and a stack
- For each number from `1` to `n`, push it to the stack, and check if the pattern in increasing or decreasing
- If the pattern is increasing or the pattern is complete, append the stack values to the result list in proper stack order (LIFO), and reset the stack
- If the pattern is decreasing, continue to the next number

## Time Complexity
$O(n)$

$n$ is the length of `pattern`.

## Space Complexity
$O(n)$