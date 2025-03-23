# Solution Walk Through
Question: https://leetcode.com/problems/shortest-common-supersequence/

## Intuition
I can utilize a buttom up DP approach with tabulation. When two characters are the same in both strings, we only need to include that character once in our supersequence. For different characters, we need to include both.

## Approach
- Initialize a 2D DP table. `dp[i][j]` represents the length of the shortest common supersequence for the first `i` characters of `str1` and the first `j` characters of `str2`.
- Set up the base cases with `dp[i][0] = i` and `dp[0][j] = j`.
- Within the loop of `n` and `m`, if the current characters match, add this character once with `dp[i][j] = dp[i-1][j-1] + 1`.
- If they don't match, take the minimum of adding either character with `dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1`
- Reconstruct the supersequence by backtracking through the DP table, and handle any remaining characters from either string.
- Reverse the result since it was built it backward and return it.

## Time Complexity
$O(n \cdot m)$

$n$ is the length of `str1`. \
$m$ is the length of `str2`.

## Space Complexity
$O(n \cdot m)$