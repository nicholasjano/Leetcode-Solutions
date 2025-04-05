# Solution Walk Through
Question: https://leetcode.com/problems/reverse-linked-list/

## Intuition
I can keep track of the previous and current nodes while going through the linked list. For each step, point the current to the previous to effectively reverse the linked list.

## Approach
- Loop through the linked list, pointing each node to its previous node
- Return the final node as the new head.

## Time Complexity
$O(n)$

$n$ represents the length of the linked list.

## Space Complexity
$O(1)$