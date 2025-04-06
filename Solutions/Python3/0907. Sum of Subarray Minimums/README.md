# Solution Walk Through
Question: https://leetcode.com/problems/sum-of-subarray-minimums/

## Intuition
I first created a brute force solution where I manually calculated the minimum subarray sum of each subarray. To make the solution more efficient, I used a monotonic stack solution. How it works is I will maintain a monotonic stack, and once a value gets popped out, add the amount of subarrays that that value would be the minimum times itself for to a total sum, and continue.

## Approach
- Loop from 0 to `n + 1`. `n + 1` is used instead of `n` for the final remaining stack values.
- If there are values in the stack, and the most recent value is smaller than the top value on the monotonic stack, run the following logic:
    - Pop the most recent index from the stack. The left bound is calculated from `popped_index - stack[-1]`, which is the left bound of the values where this value is max. If the stack if empty at this point, use `popped_index + 1` instead as it will count every value to the left. The right bound is calculated from `i - popped_index`, which is the current position in the loop subtracted by the index of the value. This is the right bound as all values inbetween will be larger than the value.
    - To find the total subarrays that number is used in, it is just left bound * right bound. Multiply that by the value in arr `popped_index` to get the sum of all subarrays where the value at `popped_index` is the minimum.
- Continue this loop until the monotonic stack remains strictly increasing.
- Append the current index to the monotonic stack.
- By the end, return the sum of all subarrays.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$