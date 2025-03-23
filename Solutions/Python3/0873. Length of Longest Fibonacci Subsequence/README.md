# Solution Walk Through
Question: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

## Intuition
I can utilize a buttom up DP approach with tabulation. Since a Fibonacci sequence requires at least 3 numbers, I can store the length of Fibonacci subsequences ending at specific pairs of indices. Since the array is sorted, I can use a two-pointer approach to find pairs that sum to a specific value.

## Approach
- Initialize a 2D DP table. `dp[i][j]` represents the length of the Fibonacci subsequence ending with `arr[i]` and `arr[j]`.
- For each index in the array starting from 2, find all pairs of previous elements that sum to `arr[curr]`. This is done using a two-pointer approach with `start` and `end`.
- Return the max length + 2 if a Fibonacci subsequence exists. Otherwise, return 0.

## Time Complexity
$O(n^{2})$

$n$ is the length of `arr`.

## Space Complexity
$O(n^{2})$