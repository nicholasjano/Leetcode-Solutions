# Solution Walk Through
Question: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

## Intuition
I can use a sliding window to find the minimum number of operations. I can maintain a max window size of `k` and count the number of white blocks in each window. With this, I can determine how many blocks need to be recolored within each window to make them all black.

## Approach
- Initialize a sliding window at 0.
- Within a loop of `blocks`, count all the white blocks up until `k` blocks have been counted.
- Afterward, for each iteration, if there is a new minimum operations within this window, update `min_operations` with the minimum amount of operations. At this point, the left pointer will move with the right pointer for the sliding window.
- Once the loop is complete, return `min_operations`

## Time Complexity
$O(n)$

$n$ is the length of `blocks`.

## Space Complexity
$O(1)$