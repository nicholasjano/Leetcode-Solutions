# Solution Walk Through
Question: https://leetcode.com/problems/meeting-rooms-ii/

## Intuition
I can sort the intervals and place the starting values in one list, and the ending values in another. I'll keep pointers at the index each pointer currently is at for each list, both starting at 0. For each iteration of the loop, if the value at the starting values list is less than the ending values list, that means a new room is needed, and that will be incremented. Vice versa, a room is now not needed and that will be decremented. Return the peak rooms at any point. 

## Approach
- Create two lists, `start_values` and `end_values` to store the start and end values of each interval respectively. Sort each list.
- Initialize pointers for each list, starting at 0.
- Loop until the `start_values` pointer is out of bounds.
- For each iteration, if the start interval at the pointer is smaller than the end interval, increment the rooms count, and update the max if needed. If the end interval at the pointer is smaller than or equal to the start interval, decrement the rooms count.
- Once the `start_values` pointer reaches `n`, return the max rooms count.

## Time Complexity
$O(n \log n)$

$n$ is the length of `intervals`.

## Space Complexity
$O(n)$