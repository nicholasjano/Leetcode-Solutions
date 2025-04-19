# Solution Walk Through
Question: https://leetcode.com/problems/put-marbles-in-bags/

## Intuition
I first came up with a backtracking solution, but this was inefficient as there is a gready solution for this problem. For the greedy solution, we can store the maximum value pairs in one heap, and minimum value pairs in another. The adjacent pairs are needed as these are the only numbers needed to calculate the scores. This ensures we only keep track of the numbers that we need for both the minimum and maximum scores. Afterward, the scores can be calculated by pulling `k - 1` times from each heap respectively.

## Approach
- Loop through each pair of weights from `weights`, adding their sum to both min heap and max heap lists.
- Heapify both lists so they can be used as heaps.
- While looping `k - 1` times for each pair needed, pop from the min heap and add the value to the minimum score, and pop from the max heap and add the value to the maximum score.
- Return the maximum score subtracted by the minimum score for the final result.

## Time Complexity
$O(n + k \log n)$

$n$ is the length of `weights`.

## Space Complexity
$O(n)$