# Solution Walk Through
Question: https://leetcode.com/problems/search-in-rotated-sorted-array/

## Intuition
I can use the condition `nums[mid] >= nums[0]` to check if mid is on the left partition, or right partition. Whether mid id on the left or not will determine which direction to move next, with mostly regular binary search logic.

## Approach
- Create traditional binary search logic. Left/right/mid pointers are all the same, and checking if the target is met is also the same.
- If the mid value is in the left array, and the target is in the left array, treat it as normal. If the target is not in the left array, the left pointer must be moved so the search gets closer or goes into the right array.
- If the mid value is in the right array, and the target is in the right array, treat it as normal. If the target is not in the right array, the right pointed must be moved so the reach gets closer or goes into the left array.
- If a value is not found, return -1.

## Time Complexity
$O(\log n)$

$n$ represents the length of `nums`.

## Space Complexity
$O(1)$