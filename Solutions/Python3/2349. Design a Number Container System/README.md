# Solution Walk Through
Question: https://leetcode.com/problems/design-a-number-container-system/

## Intuition
I need to create a data structure that can update an index with a number (change) and find the smallest index for a given number (find). A minheap needs to be used because it allows quick retrieval of the smallest index. To avoid heap deletions, I can use an auxiliary set to track valid indices and clean up values when needed.

## Approach
- Set up 3 hashmaps, `index_to_number` for mapping each index to its assigned number, `number_to_indices` for mapping each number to a minheap storing indices where it appears, and `valid_indices` for mapping sets to track which indices are still valid for each number.
- change:
    - If needed, remove the index from the old numbers `valid_indices`.
    - Assign the new number to `index_to_number`.
    - Add the index to the heap for the new number and mark it valid.
- find:
    - Check if `number` has any valid indices.
    - Remove invalid indices from the heap until the smallest valid one remains.
    - Return the smallest valid index or -1 if none exist.

## Time Complexity
$O(\log n)$

$n$ is the number of distinct indices that have been assigned numbers in the system.

## Space Complexity
$O(n)$