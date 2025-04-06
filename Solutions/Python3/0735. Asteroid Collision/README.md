# Solution Walk Through
Question: https://leetcode.com/problems/asteroid-collision/

## Intuition
I can use a stack to keep track of the current asteroids. If the final two asteroids in the stack are moving towards eachother, provide the collision logic and place the remaining asteroid (if any) back in the stack.

## Approach
- Initialize a stack to hold the asteroids.
- Loop through the asteroids, adding each to the stack.
- If the stack has 2 or more asteroids, and the final two will collide, pop the two asteroids from the stack, complete the collision logic, and place the remaining asteroid (if any) back in the stack.
- At the end, the remaining asteroids will be in the stack, so the stack will be returned.

## Time Complexity
$O(n)$

$n$ is the length of `asteroids`.

## Space Complexity
$O(n)$