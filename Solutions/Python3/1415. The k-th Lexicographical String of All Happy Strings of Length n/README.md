# Solution Walk Through
Question: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

## Intuition
I can use recursive backtracking to get each possible happy string, sort them, and then return the `k`th value.

## Approach
- Create a list holding all possible chars, as well as the final result list and a current happy string list
- Create a dfs backtracking function that goes thorugh each character, appends it to the current happy string if possible, and continues
- The current happy string is added to the result once the length reaches `n`, and characters are backtracked out of the current happy string
- Continue the dfs for every possible combination

## Time Complexity
$O(n \cdot 2^{n})$

## Space Complexity
$O(n \cdot 2^{n})$