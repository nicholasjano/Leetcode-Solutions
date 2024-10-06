# Solution Walk Through
Question: https://leetcode.com/problems/permutation-difference-between-two-strings/

## Intuition
Firstly, create a hashmap to store what index the letters occured. Loop through both `s` and `t` in the same loop. For each index, check whether the letter of `s` or the letter of `t` have been previously stored, and if they have, get the difference in indicies, and add that value to the final result.

## Approach
- Create a hashmap to store the visited charaters from both `s` and `t`.
- Loop through both `s` and `t` in the same loop.
- Firstly, check whether the current indexed character from `s` is already in the hashmap.
- If the character is already in the hashmap, that means the character has already appeared in `t`. Add the difference in indicies for the same charater in the sum.
- If the charater is not in the hashmap, add it the the hashmap, with the value being the index.
- After that process is complete for `s`, do the same thing for `t`.
- Once complete, return the sum of index differences.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(n)$