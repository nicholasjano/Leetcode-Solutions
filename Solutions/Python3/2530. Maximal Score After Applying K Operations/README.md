# Solution Walk Through
Question: https://leetcode.com/problems/maximal-score-after-applying-k-operations/

## Intuition
I can utilize a maxheap to store the highest value from `nums`. In each step, I can retrieve the highest number, add it to the score, and replace that value in the heap with `ceil(nums[i] / 3)`.

## Approach
- Turn `nums` into a maxheap.
- Loop `k` times, retrieve the highest number from `nums`, adding the value to the score, and replacing it in the heap with `ceil(nums[i] / 3)`.

## Time Complexity
$O(n + k \log n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$