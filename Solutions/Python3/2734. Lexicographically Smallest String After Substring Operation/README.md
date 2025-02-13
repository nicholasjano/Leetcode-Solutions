# Solution Walk Through
Question: https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

## Intuition
- Any character other than "a" can be decreased to be smaller lexicographically, so the substring would compose of the longest substring from the start that doesn't contain an "a". If the start starts with an "a", start the substring from the first non "a" character.

## Approach
- Check if the first character in `s` is "a".
- If it is "a", move until `s` reaches a character that is not "a". If the entire string is composed of "a"'s, then change the last character to "z" and return.
- Once a point is found where a non "a" character is found, move each character to the preceding letter using `ord()` and `chr()` until the next "a" is found. Once that next "a" is found, keep the rest of the characters the same as the substring is done.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(n)$