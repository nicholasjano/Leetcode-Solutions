# Solution Walk Through
Question: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

## Intuition
I can create a hashmap to store if each number has been visited, and if it gets repeated, add it to the resulting array. Once that array reaches 2 numbers, the code is done.

## Approach
- Initialize the hashmap and result list
- Loop through `nums`, adding each number to the visited hashmap
- If the number has already been visited, add it to the result list
- Once the result list reaches 2 values, return it

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$