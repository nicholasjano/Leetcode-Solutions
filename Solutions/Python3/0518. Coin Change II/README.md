# Solution Walk Through
Question: https://leetcode.com/problems/coin-change-ii/

## Intuition
Following a similar method to 322. Coin Change, but instead of keeping track of the smallest amount of coins to reach each amount in the dp array, I kept track of the total amount of combinations that make up that amount.

## Approach
- Initialize the dp array, where each index is the total amount of combinations that make up that amount.
- Loop through the coins, and a nested loop for each amount. Within these loops, obtain the amount of combinations for that coin/amount pair, and add that to `dp[i]` where `i` represents the current amount.
- Return the final index of the dp array, as this holds the total combinations to make the final amount.

## Time Complexity
$O(m \cdot n)$

$m$ represents the value of `amount`. \
$n$ is the length of `coins`.

## Space Complexity
$O(m)$