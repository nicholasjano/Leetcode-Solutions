# Solution Walk Through
Question: https://leetcode.com/problems/house-robber/

## Intuition
I first utilized a top-down method with memoization. I was able to eventually come up with a buttom-up approach. The subproblem that I came up with was finding the most money robbable to each index. Using this, I eventually figured out that to find out the most money robbable at any given index would be either the sum of the most money robbable to the current index and current - 2, or current index and current - 3. I know it cant be current - 4, since that value would already be taken into account when I obtained the most money robbable at current - 2.

## Approach
- Set up the base case of `n <= 2`.
- Create 3 variables that store the max money robbable for indicies 0-2.
- Begin the loop at `i=3` and calculate the new max money robbable for that index by utilizing `max(nums[3] + nums[1], nums[3] + nums[0])`. Afterward, pass the two most recent indicies (2 and 1) down one variable, as they will be used for `i=4`, and so on.
- The max between the final two indicies will be the most money robbable.

## Time Complexity
$O(n)$

$n$ is the length of nums.

## Space Complexity
$O(1)$