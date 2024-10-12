# Solution Walk Through
Question: https://leetcode.com/problems/get-equal-substrings-within-budget/

## Intuition
I can utilize a 2-pointer approach to hold the current substring bounds. I can keep adding to the right bound until the total substring cost goes over the max cost, where I would then push the left bound until the total substring cost goes under or equal to the max cost again. The longest substring at any point would be the result.

## Approach
- Initialize a loop that will run `len(s)` times, as the right bound will be incremented by 1 each loop.
- Calculate the difference of characters for the right index.
- If the difference is greater than the max cost, empty the previous substring and start a new one at the next index.
- If the difference + the current accumulated cost of the substring is greater than the max cost, remove the left bounded indicies until the difference + current accumulated cost is less than or equal to the max cost.
- Add the difference to the current accumulated cost.
- Check if the new substring has a new maximum length, and store it. This value is returned once the loop is complete.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$