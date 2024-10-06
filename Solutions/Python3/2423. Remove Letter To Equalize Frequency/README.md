# Solution Walk Through
Question: https://leetcode.com/problems/remove-letter-to-equalize-frequency/

## Intuition
I can create a frequency array for each character in the alphabet, and fill it with the charaters from `word`. I can analyze the frequencies of the characters, and there will be many edge cases to handle for the various possible situations where removing a character would work.

## Approach
- Initialize a frequency array of size 26 for each character in the alphabet.
- For each charater in `word`, increment the frequency for that characters index within the frequency array.
- Handle the rest by tracking two different frequencies and managing edge cases.

## Time Complexity
$O(n)$

$n$ is the length of `word`.

## Space Complexity
$O(1)$