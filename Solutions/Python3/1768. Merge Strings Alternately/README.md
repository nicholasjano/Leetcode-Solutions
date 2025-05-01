# Solution Walk Through
Question: https://leetcode.com/problems/merge-strings-alternately/

## Intuition
I can loop through each index up to the length of the maximum length word, and for each index, add the character from both `word1` and `word2` to the result list. I can then concatenate and return the result list.

## Approach
- Get the lengths of both words. Start a loop up to the maximum length.
- If the current index is within the length of the word, add the character at the index for each word to the result list.
- Concatenate and return the string form of the result list.

## Time Complexity
$O(n + m)$

$n$ is the length of `word1` \
$m$ is the length of `word2`

## Space Complexity
$O(1)$