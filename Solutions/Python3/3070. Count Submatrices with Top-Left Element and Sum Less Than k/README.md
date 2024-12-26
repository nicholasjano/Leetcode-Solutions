# Solution Walk Through
Question: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

## Intuition
- Starting from the top left, I can first loop down the column and get any possible submatricies, and then add the next column and repeat the same proccess, always stopping when the sum is above `k`. To obtain optimal space, I could use prefix sums for each cell value to hold the value of all previous cells in the row.

## Approach
- Create a loop that loops through the columns. For each loop, update the value of the current cell at the top row to be the prefix sum of all the previous values in the row.
- Check to see if the current column is less than `k`. If it is, add that as a submatrix. Afterward, go down the rows and see if more submatricies can be made. Same as the top row, each row will contain the prefix sum of that row.

## Time Complexity
$O(m \cdot n)$

## Space Complexity
$O(1)$