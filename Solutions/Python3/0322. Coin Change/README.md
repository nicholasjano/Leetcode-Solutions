# Solution Walk Through
Question: https://leetcode.com/problems/coin-change/

## Intuition
I initally came up with a recursive backtracking solution, and then implemented memoization into it. I later converted this to a bottom up approach, where I loop through the amounts. In a nested loop, I loop through each coin, and check if I can reach that amount in less coins. At the end of each iteration of the amounts loop, dp[i] will hold the least amount of coins needed to reach 0 from that amount.

## Approach
- Cover the base case of `amount == 0`.
- Initialize the dp array, where each index is the minimum amount of coins needed to reach 0 from that amount.
- Loop through the amounts, and a nested loop for each coin. Within these loops, look to see if each coin has a new minimum amount reach 0 and store it.
- Return the final index of the dp array, as this holds the minimum amount of coins needed for the full amount.

## Time Complexity
$O(m \cdot n)$

$m$ represents the value of `amount`. \
$n$ is the length of `coins`.

## Space Complexity
$O(m)$