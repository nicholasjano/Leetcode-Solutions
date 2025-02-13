# Solution Walk Through
Question: https://leetcode.com/problems/length-of-last-word/

## Intuition
I can loop through the string backwards, finding where the first word starts, and returning the length of that word when a space is reached. If a space is not reached and the string ends, that means there is only 1 word and the length of that word can still be returned.

## Approach
- Loop through `s` until I find the first english letter character. Once found, save that position as the start of the word.
- From there, loop until a non-english letter character (space) is found, and return the end index - the start index of the word as the length.
- If a space is never found, that means there was only 1 word, so the end index of the word + 1 will be the length of the word.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$