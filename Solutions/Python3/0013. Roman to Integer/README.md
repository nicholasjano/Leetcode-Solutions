# Solution Walk Through
Question: https://leetcode.com/problems/roman-to-integer/

## Intuition
I can loop through `s` backwards. For each value, if it has a smaller value before it, subtract the smaller value and add the larger value (such as `"IX"`). If the value before is larger, just add the number. Each character in `s` is only accounted for once, whether it was negative or positive. Keep a hashmap to store the character to value mappings. 

## Approach
- Create a hashmap to store the character to value mappings.
- Iterate starting from the back of `s`. For each loop, obtain the current and previous character.
- If the previous character has a smaller value than the current character, subtract the previous character value from the result, and decrement the position.
- Regardless, add the current character value to the result, and decrement the position.
- By the end, return the result.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$