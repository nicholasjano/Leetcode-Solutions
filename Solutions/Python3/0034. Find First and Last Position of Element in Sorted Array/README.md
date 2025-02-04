# Solution Walk Through
Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Intuition
I can do a binary search to find the leftmost occurence of `target`, and then another binary search to find the rightmost occurence of `target`.

## Approach
- Implement a binary search, but when `target` is found, continue as if the number found was actually less than target. This will ensure the leftmost occurence will be found.
- If no occurence was found, return `[-1, -1]`.
- Implement another binary search, but when `target` is found, continue as if the number found was actually more than target. This will ensure the right occurence will be found.
- Return the leftmost occurence and rightmost occurence in a list.

## Time Complexity
$O(\log n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$