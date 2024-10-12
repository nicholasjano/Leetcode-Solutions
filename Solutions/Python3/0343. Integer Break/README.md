# Solution Walk Through
Question: https://leetcode.com/problems/integer-break/

## Intuition
Utilize math to find the best number to multiply by itself to get the maximum product. The highest product in this case will include all numbers within 1 of eachother (such as 3 * 3 * 4 for 10).

## Approach
- Loop up to `n`, where each iteration hold the new divisor.
- Divide `n` by the divisor, and multiply the current product by that amount `divisor` times.
- If there is a remainer, multiply the current product by that amount + 1 `remainder` times.
- Store the highest current product from the loops.

## Time Complexity
$O(n \log n)$

## Space Complexity
$O(1)$