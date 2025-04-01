# Solution Walk Through
Question: https://leetcode.com/problems/group-anagrams/

## Intuition
For each word, I can create a list to store the counts of each letter, convert it to a tuple (so it can be used as a dictionary key), and store the word as the value. When doing this, anagrams will have the same tuple key, and will be grouped together in the dictionary without needing literal compariosn with eachother. I can then return these lists (dictionary values) as one large list for the final result.

## Approach
- Loop through each word in `strs`.
- Create a counter list that stores the occurences of each character at each index.
- Convert the counter list into a tuple, and use it as the key within the resulting dictionary, with the value as a list of words that have the same key.
- Once each word has been accounted for, return a list of the values of the resulting dictionary.

## Time Complexity
$O(n \cdot m)$

$n$ is the length of `strs`. \
$m$ is the length of the longest word in `strs`.

## Space Complexity
$O(n \cdot m)$