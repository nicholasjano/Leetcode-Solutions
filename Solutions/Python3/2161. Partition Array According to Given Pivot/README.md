# Solution Walk Through
Question: https://leetcode.com/problems/partition-array-according-to-given-pivot/

## Intuition
I can create three lists, one to store values that are less than `pivot`, one to store values that equal `pivot`, and one to store values that are greater than `pivot`. Once each number from `nums` has been added to their respective list, I can concatenate the lists and return it.

## Approach
- Create three lists: `less` to store values from `nums` less than `pivot`, `equal` to store values from `nums` equal to `pivot`, and `greater` to store values from `nums` greater than `pivot`.
- Loop through `nums`, and add each number to their respective list.
- Concatenate the three lists and return the final result.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$