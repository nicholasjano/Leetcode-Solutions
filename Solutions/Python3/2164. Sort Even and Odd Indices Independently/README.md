# Solution Walk Through
Question: https://leetcode.com/problems/sort-even-and-odd-indices-independently/

## Intuition
Create seperate lists for even-indexed and odd-indexed numbers, and sort the lists in proper order. Afterward, add the numbers one list at a time into the final list.

## Approach
- Create a list for even-indexed numbers, and another for odd-indexed numbers.
- Sort the even list in ascending order, and the odd list in descending order.
- Create a final resulting list, and append the values from the even-indexed and odd-indexed lists into the final list one at a time.

## Time Complexity
$O(n \log n)$

$n$ is the length of the nums.

## Space Complexity
$O(n)$