# Solution Walk Through
Question: https://leetcode.com/problems/longest-increasing-subsequence/

## Intuition
As for most DP questions, I first did a recursive backtracking solution, then a top down solution with memoization, than a bottom up approach with tabulation. This time, I was able to improve it even more by implementing binary search with storing the smallest possible last elements for each subsequence length instead of just storing the max subsequence length at each index.

## Approach
- For each number in `nums`, check its position in the dp array.
- If the dp array is empty or the new number is larger than any value currently in, append it to the array as this extends the longest increasing subsequence. Otherwise, find the index where this number would be inserted in the dp array with binary search, and replace that indexs value with the new number. This represents the smallest element that could be the last element of an increasing subsequence of length `index`.
- Once complete, return the length of the dp array, as this will be the length of the longest increasing subsequence.

## Time Complexity
$O(n \log n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$