# Solution Walk Through
Question: https://leetcode.com/problems/merge-two-sorted-lists/

## Intuition
I can create a new linked list that stores references of the other two linked lists as one merged list. To ensure sorting, I can take the lowest value of the two lists remaining and add it to the merged list one at a time.

## Approach
- Initialize the head and merged list with a dummy node
- While both lists are not empty, add the smallest value from either to the merged list, move to the next node and continue
- Once one list becomes empty, extend the merged list with the rest of the other list that isn't empty if applicable
- Return the head past the dummy node

## Time Complexity
$O(n + m)$

$n$ is the length of `list1`. \
$m$ is the length of `list2`.

## Space Complexity
$O(1)$