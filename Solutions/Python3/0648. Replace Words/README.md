# Solution Walk Through
Question: https://leetcode.com/problems/replace-words/

## Intuition
First, I'd use a prefix tree to map out all the root words. Afterward, for each word, I check each charater from the beginning with the prefix tree to see if there is a possible root. If there is, replace the word with the root, otherwise, keep the word as-is.

## Approach
- Setup the prefix tree to track each letter of each dictionary word. There is an "end" condition added to ensure the smallest dictionary word is always used.
- Loop through each character in each word of the dictionary, adding it to the prefix tree if it doesn't already exist from another word.
- If there is already a word in the dictionary that is shorter with the same starting characters, that full word does not need to be included, since we only need the shortest words.
- Afterward, loop through each character of each word by splitting each word into it's own value.
- If there is no possible root for the word, keep the word the same, and move onto the next word.
- If there is a possible root for the word, shorten the word to just the root, and move onto the next word.
- Rejoin all the words and return the new sentence with the updated words.

## Time Complexity
$O(M*n)$

$n$ is the total number of words in the dictionary.
$M$ is the maximum length of a word in the dictionary.

## Space Complexity
$O(M*n)$