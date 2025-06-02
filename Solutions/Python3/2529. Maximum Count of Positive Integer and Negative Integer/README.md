# Solution Walk Through
Question: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

## Intuition
My first idea was just to iterate through the list and grab the occurences of positive and negative integers. Knowing that the list was sorted, I can use binary search to find the positions of the largest negative number and smallest positive number, which can then allow me to find the total amount of positive and negative numbers, and I can efficiently return the max of both.

## Approach
- Run binary search to find the index of the rightmost negative number and store it.
- Run binary search to find the index of the leftmost positive number and store it.
- Return the maximum value between the two (with the defaults being 0 if none are found).

## Time Complexity
$O(\log n)$

$n$ represents the length of `nums`.

## Space Complexity
$O(1)$