# Solution Walk Through
Question: https://leetcode.com/problems/generate-parentheses/

## Intuition
I can use backtracking to construct each possible parentheses combination. The rules are pretty simple, as the each open must have a close afterward. This means I'd need to add an open first, and only add a closing once there are more open prior.

## Approach
- Initialize a backtracking function that keeps track of the current parenthesis string, and the amount of open/closed parentheses within the string.
- Cover the base case if the string is the max length, add it to the result list and end the branch.
- First, if the open parentheses count has not been fufilled, recursively create a new string with an extra open parentheses.
- Afterward, if the closed paretheses count is less than the open parentheses count, recursively create a new string with an extra closed parentheses.
- Return the resulting list once each combination has been made.

## Time Complexity
$O(2^{n})$

## Space Complexity
$O(n)$