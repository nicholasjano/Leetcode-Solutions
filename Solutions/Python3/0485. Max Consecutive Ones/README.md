# Solution Walk Through
Question: https://leetcode.com/problems/max-consecutive-ones/

## Intuition
Loop through the list, keeping track of the consecutive 1's. When the chain is broken, check if that was the highest chain, and save that. When the list is complete, return the saved highest chain.

## Approach
- Initialize current and maximum variables to hold the current chain and the longest chain
- Iterate through nums, if the value is 1, increment the current chain, otherwise, set maximum to the new chain only if it the new longest chain, and reset curret for the next chain

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$