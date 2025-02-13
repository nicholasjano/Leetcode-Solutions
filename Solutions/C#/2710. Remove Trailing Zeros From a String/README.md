# Solution Walk Through
Question: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

## Intuition
I can loop through `num` backwards, and once I reach a non-0 character, I can save that index and return the substring up to that point.

## Approach
- Loop through `num` until a non-0 character is reached. Once the character is reached, save `i` as the end of the substring and break out of the loop.
- Return the substring of `num` from index `0` to `i`.

## Time Complexity
$O(n)$

$n$ is the length of `num`

## Space Complexity
$O(1)$