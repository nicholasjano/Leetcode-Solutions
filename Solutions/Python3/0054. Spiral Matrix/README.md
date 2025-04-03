# Solution Walk Through
Question: https://leetcode.com/problems/spiral-matrix/

## Intuition
I can create pointers storing the rows/columns that have yet to be iterated through, as well as a variable to store the current direction. Starting right, add each element from the top row, then move the top pointer down one, and so on until the pointers overlap.

## Approach
- Initialize `top`, `bottom`, `left`, `right` variables for the current bounds.
- Create a while loop that will end once the pointers surpass eachother.
- Start navigating from `left` to `right` inclusive, adding each value to the result list. Afterward, increment `top` as the top row has been accounted for.
- Navigate down from `top` to `bottom` inclusive, adding each value to the result list. Afterward, decrement `right` as the right column has been accounted for.
- Continue this for left, up, and repeat if needed.
- Return the result list once every value has been accounted for.

## Time Complexity
$O(n \cdot m)$

## Space Complexity
$O(n \cdot m)$