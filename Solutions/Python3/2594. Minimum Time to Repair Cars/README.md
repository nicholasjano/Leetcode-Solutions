# Solution Walk Through
Question: https://leetcode.com/problems/minimum-time-to-repair-cars/

## Intuition
I can use the range of minutes it could potentially take to fix all the cars as the baseline, and conduct a binary search through that range to find the minimum minutes value with log time.

## Approach
- Set the left pointer of the binary search to 1, and the right to the length of time if only the first mechanic repaied every car.
- For each iteration, the mid value is the minutes being tested. Iterate through `ranks` to determine how many total cars can be repaired in this timeframe.
- If the total cars repaired for the current minute value is greater than or equal to `cars`, then this minute value is the new minimum time, and check smaller values. Otherwise, check for larger minute values.
- Once the binary search has completed, the minimum time value will be returned.

## Time Complexity
$O(n \cdot \log m^{2})$

$n$ is the length of `ranks`. \
$m$ is the value of `cars`.

## Space Complexity
$O(1)$