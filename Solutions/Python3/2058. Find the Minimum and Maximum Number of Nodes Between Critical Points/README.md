# Solution Walk Through
Question: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

## Intuition
I can navigate through the linked link. For each step, I will have the previous node, current node, and next node avaliable. Using these three, I can determine whether the current node is a critical point or not.

To determine the maximum range between two critical points, I can save the positions of the first ciritcal point and the final critical point.

To determine the minimum range between two critical points, I firstly set the first two critical points as the minimum distance. With every new critical point that comes in, I check if the distance between the two most recent critical points is the new minimum distance.

## Approach
- Initialize the variables to store the previous node, current node, and the variables used for determining the max/min distances.
- For each node starting from the second node, check if it is a critical point.
- If the node is a critical point, update the max/min distance variables if required.

## Time Complexity
$O(n)$

$n$ is the length of the linked list.

## Space Complexity
$O(1)$