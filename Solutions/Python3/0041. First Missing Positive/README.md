# Solution Walk Through
Question: https://leetcode.com/problems/first-missing-positive/

## Intuition
I can first loop through `nums` placing each number in their proper position. The proper position for a number is `num - 1` as that would put 1 at the 0th index, and so on. Once that is complete, I can loop through `nums` once more to find which position is missing a number. If none are missing a number, the next number (`n + 1`) would b the first missing positive integer.

## Approach
- Loop through each position in `nums`. If the current integer is within the proper range of [1, n], and it is not in the correct index, swap it to ensure it reaches the proper index. Stay at this index for the next loop to ensure that the other swapped number gets moved to the correct position.
- Once an integer in the right position or integer not in the proper range is reached, move forward in the loop.
- Once the loop is completed, all the proper integers will be in their proper indicies based off their value.
- Loop `nums` once more, checking to see if `num != i + 1`. If this condition is true, that means the positive integer of value `i + 1` is missing and can be returned.
- If every value is in the right index, return `n + 1` as it is the next missing integer.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$