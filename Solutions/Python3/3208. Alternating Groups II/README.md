# Solution Walk Through
Question: https://leetcode.com/problems/alternating-groups-ii/

## Intuition
I can loop through `colors` keeping track of the alternating streak and if it is at or above `k`, I can increment the total alteration groups by 1. If two duplicate colours occur, I'd reset the alternating streak to 1. I need to loop up to `n + k - 1` as there may be alterations including the end and start of the list as it is a circle.

## Approach
- Set variables to track the total number of alternating groups, the current alternatiing streak, and the previous color.
- Loop up to `n + k - 1`.
- Within each iteration of the loop, grab the index with `index = i % len(colors)` to ensure the loop correctly goes back to the beginning.
- If the current color is different from the previous color, continue the alternating streak, otherwise, reset the streak to 1.
- If the current alternating streak is at or greater than `k`, increment the alternating groups counter by 1 and continue.
- Once the loop has completed, return the final alternating groups counter.

## Time Complexity
$O(n + k)$

$n$ is the length of `colors`.

## Space Complexity
$O(1)$