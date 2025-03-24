# Solution Walk Through
Question: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

## Intuition
When a number is represented in base-3, each digit corresponds to a power of three. If we want to represent a number as a sum of distinct powers of three, each digit in its base-3 representation must be either 0 (don't use this power) or 1 (use this power once). If any digit is 2, we would need to use the same power of three twice, which violates the "distinct" requirement.

Ex:

- 8 in base-3: 22 \
`8 % 3 == 2` would catch this, and return False

- 10 in base-3: 101 \
`10 % 3 == 1`, `3 % 3 == 0`, `1 % 3 == 1` would return True


## Approach
- Repeatedly divide the `n` by 3 and check the remainder. If the remainder is 0 or 1, continue the division. If the remainder is 2, return False.
- Continue until `n` becomes 0, then return True.

## Time Complexity
$O(\log_{3}(n))$

## Space Complexity
$O(1)$