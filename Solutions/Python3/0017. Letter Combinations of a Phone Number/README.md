# Solution Walk Through
Question: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Intuition
I can use recursive backtracking to create every possible combination, and append it to a final result list.

## Approach
- Cover the base case if digits is empty, and return an empty list.
- Create a mapping for each number to their characters.
- Run the DFS backtracking.
- If the branch becomes of length n, add the string to the result list, as this is the end.
- If the digit is `"1"`, skip to the next number as `"1"` has no characters mapped to it.
- Otherwise, continue the search with each character from the current number.

## Time Complexity
$O(n \cdot 4^{n})$

$n$ is the length of `digits`.

## Space Complexity
$O(n)$