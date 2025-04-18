# Solution Walk Through
Question: https://leetcode.com/problems/permutations/

## Intuition
I can use recursive backtracking to create every possible permutation, and append it to a final result list.

## Approach
- Start recursive backtracking.
- Cover the base case if the current permutation reaches the max length, add it to the result list and backtrack.
- For each number in `nums`, add it to the current permutation, and continue. A check for if the current number is already in the current permutation is also done.

## Time Complexity
$O(n \cdot n!)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$