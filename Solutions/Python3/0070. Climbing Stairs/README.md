# Solution Walk Through
Question: https://leetcode.com/problems/climbing-stairs/

## Intuition
First, I utilized recursive backtracking. This is not effiicent enough, so I utilized a top-down method with memoization to cache previosuly calculated values. Afterward, to avoid recursion, I utilized a bottom-up method with tabulation. Finally, I was able to come up with a bottom-up no extra memory solution that only stores information immediately needed.

## Approach
- Cover the base case of `n <= 2`.
- Create variables `step1, step2 = 1, 2` to currently represent the outcome of `n = 1` and `n = 2`.
- Start a loop, where on each iteration, sum `step1` and `step2` for the currrent `i`, and move the `step2` value to `step1`.

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$