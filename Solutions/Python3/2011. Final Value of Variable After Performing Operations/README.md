# Solution Walk Through
Question: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

## Intuition
I found that the middle index of the string will always be the operation, so I can use that to increment or decrement `X`.

## Approach
- Loop through `operations`.
- For each loop, check if the middle index (1th index) of the string is a + or -.
- If it's a +, add 1 to `X`, otherwise, subtract 1 from `X`.

## Time Complexity
$O(n)$

$n$ is the length of `operations`.

## Space Complexity
$O(1)$