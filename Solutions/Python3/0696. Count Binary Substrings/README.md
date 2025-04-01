# Solution Walk Through
Question: https://leetcode.com/problems/count-binary-substrings/

## Intuition
I can loop through the list, keeping track of the current consecutive streak. Once a different digit appears, I compare the current streak to the previous streak. The minimum value from the two streaks represents how many valid substrings there are for that portion.

## Approach
- Look through `s`, keeping track of the current streak of consecutive `"1"`s or `"0"`s.
- Once a switch is made (from `"0"` to `"1"`), increment the valid substrings with the smallest streak between the current streak and the previous streak.
- At the end, increment again as the final streak would not have been accounted for by the loop. Then return the valid substrings count.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$