# Solution Walk Through
Question: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

## Intuition
Since this is an intervals question, I know I'd likely need to sort. Afterward, I can store the right bound of each group in a minheap, and utilize that to see whether each new interval can extent the smallest right bound group, or if a new group is needed.

## Approach
- Sort `intervals`.
- Initialize a minheap to store the right bounds of each group.
- Loop through `intervals`, and for each interval, check if the interval can extend any current group. If a current group can be extended, replace the right bound of the group to the current intervals right bound. If a current group cannot be extended, create a new group with the right bound of the interval.

## Time Complexity
$O(n \log n)$

$n$ is the length of `intervals`.

## Space Complexity
$O(n)$