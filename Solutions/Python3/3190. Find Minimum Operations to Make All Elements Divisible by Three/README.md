# Solution Walk Through
Question: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

## Intuition
This one is pretty straightforwards. After looking at the examples, I realized that for every number, it will take either 1 or 0 moves to make that number divisible by 3. I can use the modulo operator to check whether the number is already divisible by 3 or not.

## Approach
- Loop through `nums`, and for each number, check whether it is not divisible by 3 by checking if `num % 3 != 0`.
- If the number is not divisible by 3, add 1 to the total, and move onto the next number.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$