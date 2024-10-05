# Solution Walk Through
Question: https://leetcode.com/problems/relative-sort-array/

## Intuition
I'd need to first iterate through arr2 and set the priority of each number. Afterward, I'd have to use a custom sorting algorithm to sort arr1 by priority based off arr2.

## Approach
- Store the priorities of each number from arr2 in a hashmap named priorities
- Store the length of arr2 in min_other_order, to ensure that values in arr1 that are not in arr2 get an extra value added to their priority, ensureing they go at the end.
- Utilize a custom sort where for each item in arr1, if it is in priorities, sort it by it's corresponding priotity, otherwise, sort it by it's value + min_other_order to sort the ending numbers in ascending order.

## Time Complexity
$O(n \log n)$

$n$ is the length of arr1

## Space Complexity
$O(n + k)$

$k$ is the length of arr2