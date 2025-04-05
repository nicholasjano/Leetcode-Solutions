# Solution Walk Through
Question: https://leetcode.com/problems/concatenated-words/

## Intuition
I for each word in `words`, I can use that as a "search word", meaning it will be the target, and the other words will by the words to look for concatenations up to the search word. For each search word, I start from the back, moving larger and larger toward the start. Each time, I check all substring combinations to see if from this position, are there concatenations that can reach the end. By the end, if index 0 can reach the end, the search word can be added to the result.

## Approach
- Convert `words` to a set for fast lookup.
- Loop through word in `words`, setting it as the `search_word` for that iteration.
- For each `search_word`, create a dp array from 0 to the length + 1. The index at length + 1 will be set to True by default.
- Iterating through `search_word` from the end to the start, check if, starting at that index, a concatenation can be made with any remaining word(s) from `words` to the end. Since all words are unique, this will ensure that once the start index is reached, there must be at least one prior word for a full concetenation to be made.
- If a full concatenation can be made, append `search_word` to the resulting list and continue. Return the resulting list once done.

## Time Complexity
$O(n \cdot m^{3})$

$n$ is the length of `words`. \
$m$ is the average length of a word in `words`.

## Space Complexity
$O(n \cdot m)$
