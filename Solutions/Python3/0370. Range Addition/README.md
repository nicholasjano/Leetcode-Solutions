# Solution Walk Through
Question: https://leetcode.com/problems/range-addition/

## Intuition
I can use a difference array to keep track of the difference between the current value and the previous value instead of having to update every value within each update range everytime. This ensures fast complexity.

## Approach
- Create the inital array of size `length` of all zeros.
- Iterate through `updates` and increment the start index by the increment value. If the end index is not at the very end, decrement the index after the end index by the increment value.
- Once the `updates` loop has been completed, run another loop on the now-updated array of values and set each value to its prefix sum. Return the array at the end.

## Time Complexity
$O(n + k)$

$n$ represents the value of `length`. \
$k$ represents the length of `updates`.

## Space Complexity
$O(n)$