# Solution Walk Through
Question: https://leetcode.com/problems/koko-eating-bananas/

## Intuition
There is no surefire way to use math to determine the perfect value for `k`, but we know the lowest possible value and the highest possibl value. This opens up the apprach for binary search, as we have a range of possible number. Within the binary search, the amount of hours spent is counted by iterating through piles, and counting how many hours it would take to eat each pile with the current `k`.

## Approach
- Set up a binary search with left starting at 1, and right starting at `max(piles)`. Also tack the smallest `k` visited.
- The mid in this case will be the `k` value. Calculate how many hours it will take to eat all of `piles` with `k` by iterating through `piles` and calculating `ceil(pile/k)` for each pile.
- If the hours spent is less than or equal to h, this is the current smallest possible `k`. To check for smaller possible `k`, shift the right back, as if the target is on the left half of the search.
- If the hours spent is greater than h, higher `k` values need to be attempted, so the left needs to be shifted forward.
- Return the saved smallest k value.

## Time Complexity
$O(n \cdot \log m)$

$n$ is the length of `piles`. \
$m$ is the maximum value in `piles`.

## Space Complexity
$O(1)$