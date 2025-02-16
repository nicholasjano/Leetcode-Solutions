# Solution Walk Through
Question: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

## Intuition
I can create a result list, then for each open index, I can loop through n from the top down and see if the number has a possibility to fit in that spot. It will use backtracking, so if that number cannot fit in the position, it'll attempt to place the next number, and so on. A used numbers set will be needed to not repeat numbers.

## Approach
- Create the result list, filled with 0's up to the total result list length. Also create a used numbers set.
- Create a DFS backtracking function starting from index 0 of the result list.
- For the base case of `index == len(res):`, return True as the result list has been filled.
- For the base case of `res[index] != 0`, move to the next index as this index has already been filled.
- Otherwise, looping from `n` to `1`, try and add the number to the respective indicies, and add the number to the used set.
- If the number in that index cannot create a proper result, remove it from the result list and used set, and continue with the next number.
- Once a proper solution has been reached, return the result list.

## Time Complexity
$O(n!)$

## Space Complexity
$O(n)$