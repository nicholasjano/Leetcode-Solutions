# Solution Walk Through
Question: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

## Intuition
I can use a minheap to store the lowest values of each `k` list to begin. I can iterate through this heap, each time popping the smallest value, and pushing in the next smallest value from the same `k` list. By doing this, the heap will always have one value from each `k` list held, and since the smallest overall gets popped and replaced each time, each replacement gives an opportunity for a new shortest range, which is checked for after each replacement.

## Approach
- Initialize the heap, the left/right bounds, and the list that holds the current index positions of each `k` list (all starting at 0).
- Loop through `nums` once to get the first index of each `k` list pushed into the heap, and set up the initial bounds with these values.
- Iterate in a while loop to replace the smallest value in the heap with the next smallest value from the same `k` list, and update the bounds. If a new shortest range is obtained, it is saved.
- The while loop will iterate until one of the `k` lists has been depleted. Afterward, return the saved shortest range.

## Time Complexity
$O(n \log k)$

$n$ is the sum of the lengths of all `k` lists (total elements).

## Space Complexity
$O(k)$