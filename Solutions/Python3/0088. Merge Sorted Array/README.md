# Solution Walk Through
Question: https://leetcode.com/problems/merge-sorted-array/

## Intuition
I can start at the end of the values of each list (`m` and `n` respectively). If the biggest number is from `nums2`, just slot it at the end of `nums1` and move inward. Eventually if the buggest number is from `nums1`, swap the value at `nums1` with the current index later in the list, and move inward again. This will ensure that the numbers stay in order.

## Approach
- Keep track of the positions on `nums1`, `nums2`, and the total (starting at index `m + n - 1`).
- Cover the base cases if the position of `nums1` or `nums2` has been depleted, acting as if the other list has the largest value until it is depleted as well.
- If the value at the position of `nums1` is greater than `nums2`, the current index of `nums1` needs to be swapped with the current total index value, which could be the 0 placeholder.
- If the value at the position of `nums2` is greater than or equal to `nums1`, place the value from `nums2` at the current total index value.
- Decrement the current total index value by 1.
- No value needs to be returned as `nums1` is being modified in-place.

## Time Complexity
$O(n + m)$

## Space Complexity
$O(1)$