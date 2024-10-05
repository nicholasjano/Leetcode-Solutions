# Solution Walk Through
Question: https://leetcode.com/problems/longest-consecutive-sequence/

## Intuition
Since the list is unordered, I can use a hashmap to track the sequence length of the bounds of each sequence, and then save the longest sequence length to be returned at the end.

## Approach
- Firstly, nums is converted into a set to remove duplicates.
- Set up the inital variables, such as the hashmap to store the length of consecutive sequences.
- Loop through nums. For each number, check if either of the two adjacent numbers have an existing sequence length. If not, the default will be 0.
- Afterward, calculate the length of the current sequence, which will be at least 1.
- Then, update the boundaries of the sequence with the new sequence length.
- Finally, after each loop, update the max sequence length to the current sequence length if it is a new max value.

## Time Complexity
$O(n)$

$n$ is the length of nums.

## Space Complexity
$O(n)$