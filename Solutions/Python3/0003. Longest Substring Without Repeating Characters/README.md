# Solution Walk Through
Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Intuition
I can keep track of all the visited characters in a hashmap, and when a character gets visited twice, I can shift the new substring length to only include the most recent occurence.

## Approach
- Loop through the characters of `s`.
- For each character, if it has not been visited before, update the longest substring length if needed, and store the character/index pair in the hashmap.
- If the character has been visited before, and it is part of the current substring, shift the left bound to be one character ahead of the position of the previous occurence of the visited character.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$