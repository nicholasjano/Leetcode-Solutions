# Solution Walk Through
Question: https://leetcode.com/problems/palindrome-partitioning/

## Intuition
I first thought of a recursive backtracking solution using DFS, which can brute force every possible combination of substrings that are all palindromes and store them. Once I implemented it, I realized this was the only possible solution.

## Approach
- Initialize the result and current partition lists
- Start a dfs at index 0 of the string
- Introduce a base case where if the index is past the string size, add the current partition to the result list. This is because the dfs will only move forward if every substring prior is a palindrome.
- Loop from the current dfs index to the end of the string, and each time check if the substring from the dfs index `i` to the loop index `j` is a palindrome. If it is, add it to the current partition, and continue the dfs past index `j` with that substring in the current partition.
- Once the backtracking returns back a point, pop the substring from the current partition as the loop will move forward (`j`) without that substring in the current partition. This ensures all possible partitions will be taken into account.
- Once every substring has been visited, the base case will have appended all possible palindrome partitionings into the result list which can be returned.

## Time Complexity
$O(n \cdot 2^{n})$

$n$ is the length of `s`.

## Space Complexity
$O(n)$