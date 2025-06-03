# Solution Walk Through
Question: https://leetcode.com/problems/house-robber-iv/

## Intuition
There is no surefire way to use math to determine the perfect value for `steal_amount` (the robber's capability), but we know the lowest possible value and the highest possible value. This opens up the approach for binary search, as we have a range of possible numbers. Within the binary search, the number of houses that can be robbed is counted by iterating through houses, ensuring we don't rob adjacent houses, and counting how many houses have values less than or equal to the current `steal_amount`.

## Approach
- Set up a binary search with left starting at 1, and right starting at `max(nums)`. Also track the smallest valid `steal_amount` found.
- The mid in this case will be the `steal_amount` value (robber's capability). Calculate how many houses can be robbed with `steal_amount` by iterating through `nums`:
  - If a house value is less than or equal to `steal_amount`, rob it and skip the next house (no adjacent robbing)
  - Otherwise, check the next house
- If the houses robbed is greater than or equal to `k`, this is the current smallest possible `steal_amount`. To check for smaller possible `steal_amount`, shift the `right` back, as if the target is on the left half of the search.
- If the houses robbed is less than `k`, larger `steal_amount` values need to be attempted, so the `left` needs to be shifted forward.
- Return the saved smallest `steal_amount` value.

## Time Complexity
$O(n \cdot \log m)$

$n$ is the length of `nums`. \
$m$ is the maximum value in `nums`.

## Space Complexity
$O(1)$