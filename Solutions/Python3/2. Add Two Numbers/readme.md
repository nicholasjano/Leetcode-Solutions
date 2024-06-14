# Solution Walk Through
https://leetcode.com/problems/add-two-numbers/

## Intuition
For each node of the linked-lists, add their value to a new node. Save the carry over value for the next node.

## Approach
- Create a new linked-list node for the solution. Save the head value to be returned.
- Add the current values of each provided linked-list, if not None
- Use integer division to get the carry-over value, and subtract the current values accordingly
- Create the next node if needed, with the value of the carry-over

## Time Complexity
$O(n)$

## Space Complexity
$O(n)$