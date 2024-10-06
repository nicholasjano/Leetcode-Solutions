# Solution Walk Through
Question: https://leetcode.com/problems/patching-array/

## Intuition
I was initally looking for patterns between the additions, such as which sums you can get with `[1,2,3]` vs `[1,2,4]` and so on. I realized that if a patch is needed, the best number to patch will always be the number just out of the current range, so I will store that value in a variable. This greedy approach will be the most optimal solution to the problem.

## Approach
- Setup the inital variables, including `out_of_range` which represents the number just out of the current range of sums.
- Setup a while loop that will continually run until `(out_of_range - 1) < n`. When this condition is False, that means the current range has met or surpassed n, and theres no need for any more patches.
- Within the loop, first iterate through `nums` to see if any patches are needed.
- If no patches are needed, the current number is added to the `out_of_range` value, signifying a larger range with the new number.
- If `nums` has already been fully iterated through, or the current number is too large and a patch is needed, patch with the current `out_of_range` value.
- Once `(out_of_range - 1) < n` has been met, the total patches can be returned.

## Time Complexity
$O(m + \log n)$

$m$ is the length of `nums`.

## Space Complexity
$O(1)$