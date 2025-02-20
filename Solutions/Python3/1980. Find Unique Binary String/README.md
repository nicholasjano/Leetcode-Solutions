# Solution Walk Through
Question: http://leetcode.com/problems/find-unique-binary-string/

## Intuition
I can use Cantor's Algorithm to ensure the result string has at least 1 index different from each string in `nums`.

## Approach
- Create a for loop up to `n`, and for each `i`, add the opposite of `nums[i][i]` to the result string. This ensures that for every number in `nums`, at least one binary character appended will be different.

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$