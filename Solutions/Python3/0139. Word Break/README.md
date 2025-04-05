# Solution Walk Through
Question: https://leetcode.com/problems/word-break/

## Intuition
I first created a top-down solution with memoization. Afterward, I was able to convert the top-down to a bottom-up solution with a dp list. The key is to start from the end of `s`, and mark the dp array at that index to true if from that point to the end, there are words that can reach the end. This ensures that once you reach the very beginning of `s`, there could be several possible word sizes that could fufill the segmentation.

## Approach
- Convert `wordDict` to a set for faster lookup.
- Initialize the dp list up to `n + 1`, where the final index will be True, as that represents reaching the end of `s`.
- Iterate through `s` backwards. At each index of `s`, loop through the words set. If `s` starting from that index has a matching word, check if it can reach the end, either via itself, or connecting with another word. This can be done by checking if the next index after the word (`i + w`) is able to reach the end, or is the end.
- If it can reach the end, mark this index as True on the dp list, as it is possible to reach the end from this position, and break for this position.
- Continue until `s` has been fully iterated through, then return `dp[0]` which represents if `s` can go from 0 to the end of the string with any amount of words.

## Time Complexity
$O(n \cdot m \cdot k)$

$n$ is the length of `s`. \
$m$ is the length of `wordDict`. \
$k$ is the average length of a word in `wordDict`.

## Space Complexity
$O(n + m)$
