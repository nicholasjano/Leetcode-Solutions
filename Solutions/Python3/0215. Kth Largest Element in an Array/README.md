# Solution Walk Through
Question: https://leetcode.com/problems/kth-largest-element-in-an-array/

## Intuition
I can use quickselect to find the `k`th largest element. Quickselect will partition the array, and once a partition is reached where the partition splits at the index where `k` is, we can return that value.

## Approach
- Change `k` to be the index where the `k`th largest value is.
- Start Quickselect with all of `nums`.
- Pick a random index as the pivot, and swap it to the right.
- Set the pointer to be the leftmost value.
- For every other number in `nums`, if it is less than the pivot, swap it with the most recent pointer value, and increment the pointer. This will ensure numbers smaller then the pivot get swapped behind numbers larger than the pivot.
- At the end, swap the pivot with the current pointer. This will ensure all numbers on the left of the pivot are smaller than or equal to the pivot, and all the number on the right are larger than the pivot.
- If the pointer is less than `k`, that means the result is on the right partition, so rerun quicksort with this partition.
- If the pointer is greater than `k`, that means the result is on the left partition, so rerun quicksort with this partition.
- If the pointer equals `k`, the correct partition is found, and return the number at the pointer.

## Time Complexity
$O(n)$

$n$ is the length of `nums`. \

Note: In rare worst-care, the time complexity could be $O(n^{2})$

## Space Complexity
$O(1)$