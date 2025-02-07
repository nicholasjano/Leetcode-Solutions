# Solution Walk Through
Question: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

## Intuition
I can create two hashmaps, one to store the count of balls currently at each colour, one to store each balls current colour. For each query, if the colour has not been visited and I'm not removing another colour, then I can add 1 to the count. If the colour has been visited and the ball is removing another colour, I can decrement the count by 1. For each query, store the count in a result list.

## Approach
- Create the hashmaps, one to store the count of balls currently at each colour, and one to store each balls current colour.
- Loop through each query:
    - If the colour has not been visited before and the ball has not been visted before, add 1 to the count
    - If the colour has not been visited and the ball has been visited, only add 1 to the count if the ball is not making another colour have 0 balls
    - If the ball has been visited and it is at the same colour as the query, the skip over it as it is a duplicate
    - If the colour has been visited, and the ball has been visited, and the ball is making another colour have 0 balls, then decrement the count by 1
    - Ensure the ball and colour for the query are managed in the hashmaps each step
- After each loop, store the current count in the result list, and once the loop is complete, return the result list

## Time Complexity
$O(n)$

$n$ is the length of `queries`.

## Space Complexity
$O(n)$