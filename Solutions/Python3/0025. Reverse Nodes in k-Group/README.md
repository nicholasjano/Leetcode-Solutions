# Solution Walk Through
Question: https://leetcode.com/problems/reverse-nodes-in-k-group/

## Intuition
I can reverse each `k` group individually, keeping track of the end of the previous group to point to the new group once it has been reversed to ensure no disconnection.

## Approach
- Create a helper function to get the `k`th node from the current point.
- Base case if the `k`th node doesn't exist, the list has been reversed enough.
- Set the next group to be `kth.next` as `kth` is currently the end of the portion to be reversed.
- Reverse the linked list up until `kth.next` to ensure only the current group gets reversed. TO ensure no disconnection, `prev` will have an inital value of `nextGroup` so the first node (which will be the last) will point to the next group.
- Once that is done, connect the previous group with the current group by connection the end of the previous group to the new beginning of the current group, which is `kth`. Update the previous group to the new end of the current group.

## Time Complexity
$O(n)$

$n$ represents the length of the linked list.

## Space Complexity
$O(1)$