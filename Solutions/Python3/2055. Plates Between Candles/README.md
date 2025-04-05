# Solution Walk Through
Question: https://leetcode.com/problems/plates-between-candles/

## Intuition
I can use a prefix sum to keep track of the total plates at any position. This makes it easy to find the current plates in any subsection of the string. Afterward, I can get the values of the closest candles to the right and to the left of every index. This makes it so finding the bounds for plates any given query can be found in $O(1)$ time. Finally, for each query, get the leftmost and the rightmost candles, and append their plate prefix sum difference to the answers list.

## Approach
- Get the prefix sums for plates at every index.
- Get the closest candles to the right and left of each index.
- For each query, get the closest candle to the right of the left pointer (leftmost candle) and the closest candle to the left of the right pointer (rightmost candle). If they exists and are in the right order, append the prefix sum differene. Otherwise, append 0.
- Return the answers list at the end of all the query results.

## Time Complexity
$O(n + q)$

$n$ is the length of `s`. \
$q$ is the length of `queries`.

## Space Complexity
$O(n)$