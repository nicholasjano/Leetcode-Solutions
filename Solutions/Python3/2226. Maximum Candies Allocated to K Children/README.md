# Solution Walk Through
Question: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

## Intuition
There is no surefire way to use math to determine the perfect value for `candy_amount`, but we know the lowest possible value and the highest possible value. This opens up the approach for binary search, as we have a range of possible number. Within the binary search, the amount of children that can be served is counted by iterating through piles, and counting how many children can get candies from each pile with the current `candy_amount`.

## Approach
- Set up a binary search with left starting at 1, and right starting at `max(candies)`. Also track the largest valid `candy_amount` found.
- The mid in this case will be the `candy_amount` value. Calculate how many children can be served with all of `candies` using `candy_amount` by iterating through `candies` and calculating `pile//candy_amount` for each pile.
- If the children served is greater than or equal to `k`, this is the current largest possible `candy_amount`. To check for larger possible `candy_amount`, shift the `left` forward, as if the target is on the right half of the search.
- If the children served is less than `k`, smaller `candy_amount` values need to be attempted, so the `right` needs to be shifted back.
- Return the saved largest `candy_amount` value.

## Time Complexity
$O(n \cdot \log m)$

$n$ is the length of `candies`. \
$m$ is the maximum value in `candies`.

## Space Complexity
$O(1)$