# Solution Walk Through
Question: https://leetcode.com/problems/clear-digits/

## Intuition
I can loop through the string backwards, and for each digit I run into, I increment a counter for the amount of non-digit characters that need to be removed. If I run into a non-digit character and no non-digit characters need to be removed, I can add it to the final character list, and return it at the end.

## Approach
- Loop through `s` backwards, and for each iteration, check if the character is a digit or non-digit
    - If the character is a digit, increment the non-digit character removal counter by 1
    - If the character is a non-digit, and the non-digit character removal counter is over 0, decrement 1 and move on. If the non-digit character removal counter is 0, then add that character to the result list.
- Reverse and return the result list to get it back in proper form

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(n)$