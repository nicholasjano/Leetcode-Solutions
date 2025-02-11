# Solution Walk Through
Question: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

## Intuition
I can loop through the string, adding each character to the stack. If the stack ends with `part` as any point, remove those characters from the stack and continue.

## Approach
- Loop through each character in `s` and add it to the result stack
- If the stack ends with `part`, remove it from the stack and continue
- At the end, convert the stack back to a string and return it

## Time Complexity
$O(n^2)$

$n$ is the length of `s`.

## Space Complexity
$O(n)$