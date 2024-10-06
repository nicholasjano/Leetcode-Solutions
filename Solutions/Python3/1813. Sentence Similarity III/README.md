# Solution Walk Through
Question: https://leetcode.com/problems/sentence-similarity-iii/

## Intuition
I knew from this question that a double-ended queue would be useful right off the bat. I attempted some methods to save efficiency by utilizing the size of the queues, but this did not work due to edge cases. Eventually, I arrived on the fact that if I compare the left values of the sentences (index 0), popping with a match, and doing the same with the right values afterward (index -1), at least one of the queues will end up empty for true similar sentences.

## Approach
- Split each sentence into their respective words, and store them in a double-ended queue.
- Check if the leftmost values (index 0) for both words match. If they do, pop those values and check again until either one of the sentences used every word, or there is no longer a match.
- Do the same for the rightmost values (index -1) afterward.
- If either of the sentences used every word, return true as the sentences are similar.

## Time Complexity
$O(n + m)$

$n$ is the length of `sentence1`. \
$m$ is the length of `sentence2`.

## Space Complexity
$O(n + m)$