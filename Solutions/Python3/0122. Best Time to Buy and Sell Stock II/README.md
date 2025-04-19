# Solution Walk Through
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## Intuition
For each day, if the stock price the next day is higher, I can buy the stock the current day, and sell it the next day.

## Approach
- Loop up to `n - 1` to avoid out of bounds errors.
- On each day, if the current price is less than the price on the next day, add the difference as the stock will be bought today and sold tomorrow.

## Time Complexity
$O(n)$

$n$ is the length of `prices`.

## Space Complexity
$O(1)$