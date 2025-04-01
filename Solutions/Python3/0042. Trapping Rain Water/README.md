# Solution Walk Through
Question: https://leetcode.com/problems/trapping-rain-water/

## Intuition
I can utilize a two pointer approach with the pointers starting on each end of `height`. For each step, whichever pointer is at a lower height will move one step twoards the middle. This ensures that when the pointer moves one step towards the middle, the other pointer will be just as high or higher, meaning any drop in height when moving toward the middle will be trapped rain water.

## Approach
- Cover the base case if `height` is two or less, and return 0 as it is impossible to trap any rain water under these conditions.
- Set up the left and right pointers at each end of `height`, and set up variables to store the max left and max right values.
- Create a while loop with the condition `left < right` so the loop will end when the pointers meet.
- Within the loop, for each iteration, select the pointer with the smallest height to move towards the center. If the pointers are tied, move the right pointer.
- After the pointer moves, recalculate the max left or max right value depening on which pointer moved, and check if there is any drop in height compared to the max. If there is, add the difference to the trapped rain water.
- Once the pointers meet, exit the loop and return the summed trapped rain water value.

## Time Complexity
$O(n)$

$n$ is the length of `height`.

## Space Complexity
$O(1)$