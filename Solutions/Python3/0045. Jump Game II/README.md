# Solution Walk Through
Question: https://leetcode.com/problems/jump-game-ii/

## Intuition
I can utilize a greedy BFS-like approach where there are "buckets" for each jump (ex: in best case with x jumps you can get in this range). Within each bucket, i find the max range of the next bucket by checking where the furthest jump can be made.

## Approach
- Cover the base case if `n == 1`, return 0.
- Create left and right pointers for the boundaries, both starting at index 0.
- Within the boundry, find the furthest index to jump. Set the left pointer to the start of the next bucket, and the right pointer to the furthest index to jump (end of the bucket).
- If the right pointer every reaches or surpasses the final index, return the total buckets (jumps) needed.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$