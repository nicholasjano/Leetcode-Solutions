# Solution Walk Through
Question: https://leetcode.com/problems/longest-common-prefix/

## Intuition
Loop through each index of the strings and see if they match. Exit and return the prefix when there is a divergence.

## Approach
- Create an empty prefix string and index counter
- Create a while loop with a condition to ensure counter does not index too high
- Run a for loop for each string to see if they all match the current character at index counter
- If they all match, increment counter, add the character to the prefix and loop again
- If a string reaches is max length, or a string does not have a matching character, return the prefix

## Time Complexity
$O(n \cdot L)$

$n$ is the amount of strings.

$L$ is the length of the shortest string.

## Space Complexity
$O(L)$