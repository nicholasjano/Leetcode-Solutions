# Solution Walk Through
Question: https://leetcode.com/problems/subarray-sum-equals-k/

## Intuition
I can track the prefix sum while traversing through `nums`. For each prefix sum, I will store it in a hashmap, along with how many occurences it has. If I come across a number that needs to subtract a previous prefix sum to reach `k`, then I know that there is a valid subarray, as if I removed all the values before that subtracted prefix sum, then I would get the valid subarray.

## Approach
- Setup the `prefix_sums` dictionary. Initially set 0 to 1 to ensure exact prefix sums equalling `k` from the start get accounted for.
- Loop through `nums`, add to the prefix sum, and find if the difference has been visited before or is 0. If it has, add the amount of visits the difference has to the total valid subarrays.
- Afterward, increment the prefix sums at the current prefix sum for future use (it could be a difference later).
- Once the loop is completed, return the total valid subarrays.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$