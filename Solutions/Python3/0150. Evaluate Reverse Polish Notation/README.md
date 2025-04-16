# Solution Walk Through
Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Intuition
I can use a stack to keep track of the most recently appended numbers, and preform operations when needed. This ensures the program maintains order of operations.

## Approach
- Loop through tokens.
- If the current token is a number, add its int equivalent to the stack.
- If the current token is a operator, pop the two most recent numbers, preform the operation, and add the result back to the stack.
- By the end, return the 0th index of the stack as the overall result.

## Time Complexity
$O(n)$

$n$ represents the length of `tokens`.

## Space Complexity
$O(n)$