# Solution Walk Through
Question: https://leetcode.com/problems/integer-to-roman/

## Intuition
I can create a mapping to store each roman number digit combo with their cooresponding value. Afterward, I can loop through the mapping, checking how many occurences of each there are, and adding it to a result list.

## Approach
- Create a mapping to store each value/symbol pair in descending order.
- Loop through the mapping, and check the occurences of each mapping with `num // value`. The count of the symbol will be added to the result list.
- `num %= value` will be ran to remove the accounted for occurences from `num`.
- At the end of each loop iteration, check if `num` is now 0, and break.
- At the end, concatenate and return the resulting list of symbols.

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$