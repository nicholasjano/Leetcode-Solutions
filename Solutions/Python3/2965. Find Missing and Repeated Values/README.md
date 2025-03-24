# Solution Walk Through
Question: https://leetcode.com/problems/find-missing-and-repeated-values/

## Intuition
I can use a hashmap to store the frequencies of each number in `grid`. Thereafter, I can figure out which number from $[1, n^{2}]$ appears twice (`a`), and is missing (`b`).

## Approach
- Store the frequencies of each number in a hashmap.
- Loop through each number from $[1, n^{2}]$. If the number has a frequency of 2, set it as `a`. If the number has a frequency as 0, set it as `b`.
- Return the pair of `a` and `b`.

## Time Complexity
$O(n^{2})$

## Space Complexity
$O(n^{2})$