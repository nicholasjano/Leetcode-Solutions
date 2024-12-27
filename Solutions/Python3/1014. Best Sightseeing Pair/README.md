# Solution Walk Through
Question: https://leetcode.com/problems/best-sightseeing-pair/

## Intuition
I can use a bottom-up approach, storing the highest value index as `i`, and looping through the rest of the list as `j`, and saving the max value as I go.

## Approach
- Start with `i` as index 0, and loop from `1..len(values)`.
- If at any point the current `j` yields a higher value than `i`, store `j` as the new `i`.
- If at any point the new value with the current `i` and `j` is greater than the previous highest value, store that value as the new highest value.
- Once the full list has been iterated though, return the saved highest value.

## Time Complexity
$O(n)$

$n$ is the length of `values`.

## Space Complexity
$O(1)$