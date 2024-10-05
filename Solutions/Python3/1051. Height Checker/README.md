# Solution Walk Through
Question: https://leetcode.com/problems/height-checker/

## Intuition
First instinct is to sort the heights array and store it as a new array and compare each index.

## Approach
- Save the sorted values of heights in a new array named "expected"
- For each value in heights, check if expected[i] != heights[i], and add 1 is the resulting counter if the condition is true.
- Return the counter to show the amount of misplaced heights.

## Time Complexity
$O(n \log n)$

$n$ is the length of heights.

## Space Complexity
$O(n)$