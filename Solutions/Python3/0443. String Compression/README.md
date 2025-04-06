# Solution Walk Through
Question: https://leetcode.com/problems/string-compression/

## Intuition
I can keep track of the current position to write in with a pointer, and navigate the string until a new character is found. Once a new character is found, write the character, and its respective count infront of it if the count is above 1. At the end, run the writing for the final character as if a new character was found infront of it.

## Approach
- Cover the base case if `chars` is empty, return 0.
- Create a variable to keep track of the current position to write in, and another variable to keep track of the count of the current character.
- Loop though `chars`, incrementing the count for each duplicate character.
- Once a new character is found, write the old character and its count using the write variable position, and continue for the new character.
- At the end, ensure that the final character has been accounted for, treat the end as if a new chracter was found.
- The final write position is the length of the final updated list, so it is returned.

## Time Complexity
$O(n)$

$n$ is the length of `chars`.

## Space Complexity
$O(1)$