# Solution Walk Through
Question: https://leetcode.com/problems/two-sum/

## Intuition
For each value, check if we've passed it's needed compliment before. Each value will be saved to check for needed compliments.

## Approach
- Create a hashmap to store passed list values, with their index as the value
- For each value in `nums`, check if `target - nums[i]` (the compliment) is in the hashmap.
- If the compliment exists, place the indicies in an array and return it.
- If the compliment does not exist, place the value and index into the hashmap and keep looping.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$