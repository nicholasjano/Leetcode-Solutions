# Solution Walk Through
Question: https://leetcode.com/problems/reduce-array-size-to-the-half/

## Intuition
I know I could use a greedy approach, and the fastest way to get to the target of half is to remove the largest occurenced numbers one by one. I can use a Counter to get the occurences of each number, and then place the occurences in a max heap, and pop then one by one until I surpassed the targer.

## Approach
- Create a Counter to count the occurences of all numbers in `arr`
- Place all the occurences in a max heap
- Go through the max heap one at a time, subtracting the highest occurence value until the target of half the size has been met
- Return the amount of iterations of the loop as the set size

## Time Complexity
$O(n \log n)$

$n$ is the length of `arr`.

## Space Complexity
$O(n)$