# Solution Walk Through
Question: https://leetcode.com/problems/container-with-most-water/

## Intuition
I can utilize a two pointer approach with the pointers starting on each end of `height`. The area can be calculated by the minimum height between two points, multiplied by their distance. Whichever height is smaller will move towards the middle until the pointers overlap.

## Approach
- Set up the left and right pointers at each end of `height`, and set up a variable to store the max area.
- Create a while loop with the condition `left < right` so the loop will end when the pointers meet.
- Within the loop, for each iteration, calculate the area between the two pointers and update the max area if applicable.
- Afterward, select the pointer with the smallest height to move towards the center. If the pointers are tied, move the right pointer.
- After the pointer moves, recalculate the area and max area, and continue the loop.
- Once the pointers meet, exit the loop and return the saved max area.

## Time Complexity
$O(n)$

$n$ is the length of `height`.

## Space Complexity
$O(1)$