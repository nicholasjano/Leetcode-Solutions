# Solution Walk Through
Question: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

## Intuition
I can convert `nums` into a minheap, and then create a loop where I pull the top two numbers from it, check if the smallest number is greater than `k`, and if not, calculate `min(x, y) * 2 + max(x, y)` for the smallest 2 numbers and put it into the heap and repeat.

## Approach
- Convert `nums` into a minheap
- While the length of the heap is above 2, pull the top two numbers from the heap
- If the smallest number is greater than `k`, then the condition is met and the operations can be returned
- If the smallest number is not greater than `k`, then calculate `min(x, y) * 2 + max(x, y)` for the smallest 2 numbers and put it into the heap, and increment the operations by 1
- Loop until there aren't enough numbers left or the smallest number is greater than `k`

## Time Complexity
$O(n \log n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$