# Solution Walk Through
Question: https://leetcode.com/problems/jump-game/

## Intuition
I First completed a recursive backtrack approach where I tried every single possible case. This was slightly optimized with memoization. Afterward, I created a bottom-up approach with a DP array, followed by a bottom-up approach with constant memeory. How the bottom-up approach with constant memory works is I set a variable to hold the threshold needed to jump to the end, which starts at the end. I can loop from the second last index in `nums`, if it can jump to the threshold, it will be the new threshold. This greedy approach ensures that only the most important data is saved, leading to constant memory.

## Approach
- Set `min_reachable` to the end of the list as the current threshold needed to jump.
- Loop through `nums` backwards starting from the second last number.
- If the number can jump to the treshold, make the current index the new threshold.
- If the number cannot jump to the theshold, continue the loop with the next number.
- By the end, if the threshold equals 0, that means from the start of `nums`, a path to jump to the end is possible. This is why if the threshold equals 0 return True, otherwise return False.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$