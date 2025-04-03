# Solution Walk Through
Question: https://leetcode.com/problems/copy-list-with-random-pointer/

## Intuition
I first came up with a hashmap solution that could store the values, but this is not needed as I can create a three pass method. In the first pass, I create new nodes ahead of the original nodes with the same value. This will double the size of the linked list for now. In the second pass, I can now assign the new nodes their random values based off of the original values. Finally, in the thrid pass I can split the two linked lists, enforcing that the new linkedlist will not have any connection to the old one.

## Approach
- Cover the base case if `head` does not exist, and return None.
- Go through the first pass, creating new nodes inbetween each node, copying the value of the previous node.
- Go through the second pass, updating the ransom values for the new nodes, based off the information provided on the old nodes.
- Go through the third pass, skipping a node with each next, effectively splitting the two linked lists.
- Return the linkedlist with the new nodes.

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$