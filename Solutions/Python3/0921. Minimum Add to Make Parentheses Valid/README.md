# Solution Walk Through
Question: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

## Intuition
When traversing the string from left to right, if at any point there are more closed brackets compared to open brackets, that means there must be an open bracket inserted prior. By the end, any extra open brackets will have an equal amount of closed brackets inserted.

## Approach
- Look through each char in `s`, keeping track of the balance of open to closed brackets visited. If at any point there are more closed brackets than open brackets, add an insertion, and update the balance.
- Once the loop is complete, add any extra insertions for closed brackets needed based off the final balance.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$