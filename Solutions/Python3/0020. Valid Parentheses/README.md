# Solution Walk Through
Question: https://leetcode.com/problems/valid-parentheses/

## Intuition
I can use a stack to store the parentheses. If the two most recent values in the stack compliment eachother (opening and closing), then they can be removed from the stack. By the end of the string traversal, if the stack is empty, `s` is a valid string.

## Approach
- Cover the base case if `s` has an odd length, as the result will always be False.
- Loop though each character in `s`, adding it to the stack.
- If the stack has a length of 2 or greater, check if the final 2 characters make a proper paratheses structure. If they do, pop them out of the stack.
- After the loop is completed, if the stack is empty, return True. Otherwise, return false.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(n)$