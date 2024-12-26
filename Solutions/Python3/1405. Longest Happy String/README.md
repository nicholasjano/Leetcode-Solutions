# Solution Walk Through
Question: https://leetcode.com/problems/longest-happy-string/

## Intuition
I can use a greedy appraoch by keeping track of the most common character, placing it twice, then placing the second most common character afterward. This process repeats until there are no more avaliable characters to keep the string happy.

## Approach
- Use a counter to store all the max occurences of each character.
- Starting a loop, grab the two most common characters.
- If the most common character has not been included as part of the two most recent characters, add it to the resulting string.
- If the most common character cannot be added, add the second most common character to the resulting string.
- Once the character to be added has no more possible occurences, the maximum string length has been reached.

## Time Complexity
$O(n)$

$n$ is the sum of `a`, `b`, `c`.

## Space Complexity
$O(1)$