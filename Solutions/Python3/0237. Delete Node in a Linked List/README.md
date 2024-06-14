# Solution Walk Through
Question: https://leetcode.com/problems/delete-node-in-a-linked-list/

## Intuition
Since we know the node is not the tail, we can copy the value of the next node, and skip past its original state. This effectively moves the next node back 1, leaving no space for the node we deleted.

## Approach
- Set the current node value to the value of the next node. The current node will be converted into what the next node was.
- Set the proper next value, from what the other node had. This ensures the current node fully copied the next node, so it can be removed without any loss of data.

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$