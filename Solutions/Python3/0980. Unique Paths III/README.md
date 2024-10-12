# Solution Walk Through
Question: https://leetcode.com/problems/unique-paths-iii/

## Intuition
I can utilize a DFS backtracking solution to find all paths from the start point to the end point. I can keep track of the amount of total moves required to ensure by the time I went from start to end, every tile has been passed.

## Approach
- Loop through the grid to obtain the start coordinates and the amount of obstacles. 
- Utilize a DFS to move in each direction for each cell.
- For each traversal, mark a visited cell with -1 so it does not get visited again within that traversal.
- Once complete, sum the valid paths of traversals from all 4 directions and return.

## Time Complexity
$O(3^{m \cdot n})$

## Space Complexity
$O(m \cdot n)$