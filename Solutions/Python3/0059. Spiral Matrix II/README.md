# Solution Walk Through
Question: https://leetcode.com/problems/spiral-matrix-ii/

## Intuition
Create an extra list to store the spiral-ordered values. Have a flag that holds the current moving direction (right, left, down, up). Once a barrier in one direction has been reached, I will update the flag with the new direction. There will be counters to shorten the barrier as the spiral goes on, as the navigation will need shorter movements per direction as it approches the center. This is a very similar approach to 54. Spiral Matrix.

## Approach
- Declare inital variables that will be used in the loop.
- In each iteration of the loop, update the current position on the final list.
- Run an if statement to check the current direction. If the next move is in the same direction, update the current position to the next position in that direction. Otherwise, update the moving direction flag, and move in the new direction.

## Time Complexity
$O(n^2)$

## Space Complexity
$O(n^2)$