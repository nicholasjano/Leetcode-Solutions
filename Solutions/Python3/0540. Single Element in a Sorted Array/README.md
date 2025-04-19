# Solution Walk Through
Question: https://leetcode.com/problems/single-element-in-a-sorted-array/

## Intuition
I can use binary serach with a different comparison mechanism. If the numbers to the left and right are different than the mid value, then we know we have our value. Otherwise, if we're on the left value of the pair, and the remaining left values are an equal number, that means that the single number is on the right side. Same can be applied vice versa.

## Approach
- Begin a binary search.
- Cover the base cases if the mid value is on either end of the list, checking if the current value is the result, or which direction to go in.
- If the current mid value is equal to the previous value, that means the current number is at the end of a pair. If the amount of elements to the right are even, that means the result is on the left half, so update the right pointer. Otherwise, update the left pointer.
- If the current mid value is equal to the next value, that means the current number is at the beginning of a pair. If the amount of elements to the left are even, that means the result is on the right half, so update the left pointer. Otherwise, update the right pointer.
- If the current mid value is not equal to either the previous or next values, return that number as the result.

## Time Complexity
$O(\log n)$

## Space Complexity
$O(1)$