# Solution Walk Through
Question: https://leetcode.com/problems/rotting-oranges/

## Intuition
My first thought was to detect a rotten orange, then rot any connected oranges, similar to the Number of Islands problem. The difference here is that there can be several rotten oranges that can rot a single orange, meaning I'd need to find the closest original rotten orange for each orange to minimize time. I can use a multi-source BFS to accomplish this goal.

## Approach
- Place all the rotten oranges in a queue, and keep track of the total fresh oranges.
- If there are no fresh oranges, return 0.
- Utilize BFS to iterate through the grid. For each cell in the queue, spread the rot to any avaliable 4-directionally adjacent cell with a fresh orange. Update the fresh orange count accordingly.
- Once the BFS has been completed, if there are still fresh oranges left, return -1 as there are isolated fresh oranges. If there are no fresh oranges left, return the max level the BFS reached as the minutes.

## Time Complexity
$O(n \cdot m)$

## Space Complexity
$O(n \cdot m)$
