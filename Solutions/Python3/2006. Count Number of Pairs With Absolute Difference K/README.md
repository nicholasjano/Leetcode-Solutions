# Solution Walk Through
Question: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

## Intuition
First thought is to just brute-force and check every pair. This is not efficient, and I came up with a method that involves a hashmap. Basically I can loop though `nums`, and check if any of the complements are stored in the hashmap (num - k or num + k). This would represent a pair. At the end of each loop, I store the value in the hashmap so future numbers can use it as a complements.

## Approach
- Initialize the `visited` hashmap and the pairs counter.
- Loop through nums, checking if either complement (num - k or num + k) already exists in the hashmap. If they do, add the current frequency of the complement(s) to the pairs counter.
- At the end of each loop, increment the frequency of the current number within the hashmap.

## Time Complexity
$O(n)$

$n$ is the length of nums.

## Space Complexity
$O(n)$