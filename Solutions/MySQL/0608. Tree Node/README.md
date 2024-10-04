# Solution Walk Through
Question: https://leetcode.com/problems/tree-node/

## Intuition
First I'd check if a node is the root by checking if p_id is null. After, I can check if that node's id exists anywhere in p_id, making it an inner node. Any other node is a leaf.

## Approach
- Select id from tree
- Within the select, include a case that checks if a node is a root, inner, or leaf
- To determine a root, p_id must be null for that node
- To determine an inner, the node id must be the p_id of another node
- Finally, if a node is not a root or inner node, we can say it is a leaf node