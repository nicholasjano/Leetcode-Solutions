# Solution Walk Through
Question: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

## Intuition
I can use prefix sums to solve this problem. A subarray has an odd sum if and only if its prefix sums have different parities (one even, one odd). By tracking how many even and odd prefix sums seen, we can count the number of subarrays with odd sum.

## Approach
- Initialize variables for count, prefix sum, odd prefix sums, and even prefix sums
- Loop through each number in `arr`, adding it to the prefix sum
- If the current prefix sum is even, any subarray ending at the current element and starting after an odd prefix sum will have an odd sum.
- If the current prefix sum is odd, any subarray ending at the current element and starting after an even prefix sum will have an odd sum.
- Update the counters for even and odd prefix sums accordingly, including using the MOD on the overall count.

## Time Complexity
$O(n)$

$n$ is the length of `arr`.

## Space Complexity
$O(1)$