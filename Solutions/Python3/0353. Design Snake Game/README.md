# Solution Walk Through
Question: https://leetcode.com/problems/design-snake-game/

## Intuition
I can use a double ended queue to store the snakes positions for order, as well as a set to store the snakes positions for quick lookup. When `move()` is called, new row/column values will be created. If either value is out of bounds, end the game by returning -1. If the new position eats the food, increment the score and don't remove the tail, otherwise, remove the tail. Afterward, I can check if if snake has a collision with itself, and return -1 if it does. At the end, add the new head and continue.

## Approach
- `__init__()`:
    - Set up the inital variables.
    - Set up a queue and set to store the dynamic snake data.
    - Create a hashmap to store movements for each movement input.
- `move()`:
    - Calculate the position of the new head. Return -1 if it is out of bounds.
    - Check if the new position eats the current food. If it does, increment the score and don't remove the tail. If the food is not eaten, remove the tail.
    - Check if the snake overlaps with itself and return -1 if it does.
    - Add the new position as the head of the snake and return the score.

## Time Complexity
`__init__()`: $O(1)$ \
`move()`: $O(1)$

## Space Complexity
$O(n)$

$n$ is the maximum length of the snake.