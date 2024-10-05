# Solution Walk Through
Question: https://leetcode.com/problems/subarray-sums-divisible-by-k/

## Intuition
Seeing the word "divisible" in the problem made me think that I need to use the modulo operator. I can use a running sum to check if the full array up to that point is divisible by k, or I can also see if the array from any point up to that point is divisible by k by storing previous remainders in a hashmap.

## Approach
- Setup the hashmap with 0: 1 as the inital value, as if the remainer is 0, that should be at least 1 subarray.
- Loop through the numbers, keeping the running sum held in the "sum" variable.
- If the remainder is not in the hashmap, store the value 1, as if that remainder is reached again, there will be a subarray from the first occurence to the next occurence.
- If the remainder is already in the hashmap, you add the cooresponding value to subarrays, and you increment that index of the hashmap by 1. This is to ensure all subarrays of all sizes are properly accounted for.
- Return the amount of subarrays once the loop has completed. There are no possible breaks within the loop.

## Time Complexity
$O(n)$

$n$ is the length of nums.

## Space Complexity
$O(k)$