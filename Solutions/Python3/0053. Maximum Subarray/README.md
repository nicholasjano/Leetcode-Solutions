# Solution Walk Through
Question: https://leetcode.com/problems/maximum-subarray/

## Intuition
I can first use recursive backtracking to create a solution. This isn't efficient, so I think went to a bottom-up approach with a dp arrap. I noticed that only the past value was used to update the new value, so I came up with a no memory approach. For each number, it's max subarray sum is either itself, or itself + previous values.

## Approach
- Cover the base case if `n` is 1, just return the number.
- Set the current value to `nums[0]`.
- For each iteration though nums, the maximum subarray sum at that point will be either itself, or itself + the previous value. Allowing it to just be itself helps remove earlier negatives.
- On each step, keep track of the maximum subarray sum, as it is not neccesarily always at the end. 

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$