# Solution Walk Through
Question: https://leetcode.com/problems/random-pick-with-weight/

## Intuition
I can first change the value of each element in `w` to be their respective probabilities, as well as a prefix sum to ensure the gap between two indicies is the probability of the second index. This is done to create a number line from 0-1, where if I generate a random number from 0-1, the insert position index of the random number into the number line list is the same index that needs to be returned.

## Approach
- Convert `w` into into a list holding the prefix sum of the probabilities at each index.
- When `pickIndex` is called, generate a random floating point number from 0-1.
- Find the insert position of the random number on the new `w` list using binary search, as that will be the index to return.

## Time Complexity
$O(n)$

$n$ is the length of `w`.

## Space Complexity
$O(n)$