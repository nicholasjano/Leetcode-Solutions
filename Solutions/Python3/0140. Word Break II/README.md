# Solution Walk Through
Question: https://leetcode.com/problems/word-break-ii/

## Intuition
I can use a recursive backtracking approach on `s` starting from index 0. From the start point to the end point (which can be anywhere from one character to the end of `s`), if a word in `wordDict` can be made, continue the backtracking forward, now starting from the end index. If the end can be reached, backtrack to append each word from the back to the front in the sequence to a resulting list. 

## Approach
- Convert `wordDict` into a set for efficient lookup.
- Start the backtracking from index 0.
- Cover the base case if the index equals `n`, and return a list containing the empty string as an indication the end has been reached.
- Cover the base case if the index has already been visited via memoization, and return the result.
- Loop from the start index to the end of `s`, creating a word between the indicies. If the word is in `wordDict`, recursively continue, now starting from the end index.
- By the end of the branch, if the word combinations can reach `n`, backtrack and add each word/sentence to the result.
- By the time the backtracking reaches index 0, the full sentences will be appended to the result list, and returned.

## Time Complexity
$O(2^{n})$

$n$ is the length of `s`.

## Space Complexity
$O(2^{n})$
