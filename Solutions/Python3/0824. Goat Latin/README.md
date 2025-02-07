# Solution Walk Through
Question: https://leetcode.com/problems/goat-latin/

## Intuition
I can split the sentence into a list of words, and then loop through the words, applying the rules at for each string, and overwriting the original words with the updated words.

## Approach
- Split `sentence` into a list of words
- For each word, test if it starts with a constant or a vowel, and apply the rule for that starting character
- Concatenate `"ma"` to the end of the word, as well as `"a" * (i + 1)` for the final rules
- Overwrite the updated word to the words list, and when done looping though every word, return the string version of the words as a sentence in Goat Latin

## Time Complexity
$O(n^2)$

$n$ is the length of `sentence`.

## Space Complexity
$O(n)$