# Solution Walk Through
Question: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

## Intuition
I can keep a pointer for my current position for both `nums1` and `nums2` starting from 0, and whichever has the lowest ID value will be added to the resulting list. If they both have the same ID value at their current positions, then the corresponding values will be summed and added to the resulting list.

## Approach
- Initialize pointers for `nums1` and `nums2`, both starting at 0 (front of the list).
- Create a while loop that will loop until either pointer passes its respective list.
- Within the loop, check which list has a lower ID value at their current positions.
- If one list has a smaller ID value than the other, append the value at the current index into a result list, and increment the current position.
- If both lists have the same ID value, sum their values together, and append the ID and summed value to the result list as a pair.
- Once the loop exits, append any leftover values from one of the lists to the resulting list.
- Return the resulting list.

## Time Complexity
$O(n + m)$

$n$ is the length of `nums1` \
$m$ is the length of `nums2`

## Space Complexity
$O(n + m)$