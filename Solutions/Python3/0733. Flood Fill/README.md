# Solution Walk Through
Question: https://leetcode.com/problems/flood-fill/

## Intuition
I can use BFS starting at the pixel at `image[sr][sc]`, turning the pixel to the new color, and adding the 4 adjacent pixels to the BFS queue if they are within bounds and the same color as the initial pixel.

## Approach
- Cover the base case if the initial pixel value at `image[sr][sc]` already matches the desired colour, and return `image`.
- Place the initial pixel into a queue, and naviagate the grid using BFS.
- For each pixel in the queue, change the value to `color`, and add the adjacent pixels to the queue if they are within the bounds of the grid, and they match the initial colour.
- Return the updated `image`.

## Time Complexity
$O(n \cdot m)$

## Space Complexity
$O(n \cdot m)$
