# Solution Walk Through
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Intuition
I can loop through prices, keeping track of the current smallest and current largest values. If the current smallest value is updated, also update the current largest as previous days should not be taken into account. Whenever the current largest is updated, there is an opportunity for there to be a new largest gap to store and return.

## Approach
- Create variables to store the current smallest and current largest values. Initialize both of them to `prices[0]`.
- Loop the rest of `prices`. If a new smallest value is found, update both variables to this value as the previous larger values will be irrelevant.
- If a new largest value is found, update only the largest value. This will ensure that a gap is created.
- If the gap is larger than the current max gap, update the max gap.
- Once completed, return the max gap.

## Time Complexity
$O(n)$

$n$ is the length of `prices`.

## Space Complexity
$O(1)$