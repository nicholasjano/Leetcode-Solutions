# Solution Walk Through
Question: https://leetcode.com/problems/build-array-from-permutation/

## Intuition
Looping through the list, I can simply follow the question and assign `ans[i] = nums[nums[i]]` where `ans` represents a new list. Moreover, this can be done with list comprehension.

## Approach
- Create a list comprehension that assigns the new list the value of `nums[nums[i]]` for each `i`.

## Time Complexity
$O(n)$

$n$ is the length of nums.

## Space Complexity
$O(n)$