# Solution Walk Through
Question: https://leetcode.com/problems/k-concatenation-maximum-sum/

## Intuition
I can run through the array three times, keeping track of the running current subarray sum and max subarray sum. This effectively makes `arr = arr * 3`. This is needed as if I see the first two runs have the same max subarray sum, then I know that as `k` grows, the max subarray sum stays the same. Same is applied for if the second and third runs have the same max subarray sum, then I also know that as `k` grows, the max subarray sum stays the same. Only when all 3 runs have an increasing max subarray sum, then I can return `base + (k * difference)` where `difference` is the amount the max subarray sum increases by per run, and `base` is the base value to increment.

## Approach
- Set up a loop to run three times
- Within the loop, calculate the running maximum subarray sum and current subarray sum values for `arr`
- At the end of each loop, check base cases to ensure it doesn't run it more than `k` times, and that the maximum subarray sum is increasing per iteration
- If a condition is found where the maximum subarray sum is not increasing, return the maximum subarray sum
- Once the loop has been completed, if the maximum subarray sums are all increasing, calclulate how big the final maximum subarray sum would be after `k` runs, with proper MOD considerations

## Time Complexity
$O(n)$

$n$ is the length of `arr`.

## Space Complexity
$O(1)$