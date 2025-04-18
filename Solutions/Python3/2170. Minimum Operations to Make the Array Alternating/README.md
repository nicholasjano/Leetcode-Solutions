# Solution Walk Through
Question: https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

## Intuition
I can first create sublists containing just the even numbers and just the off numbers, and create a counter dictiionary for both. For there, I can store the top two most frequent values from each. These are needed as the amount of swaps is the length of the sublist minus the frequency of the top element. The top two elements are needed from both to cover the edge case that considers if both the even and odd sublists have the same most frequent value.

## Approach
- Cover the base case if `n` is 0 or 1, just return 0 as no swaps are needed.
- Create two sublists and fill them with the even indexed numbers from `nums`, and the odd indexed numbers from `nums`, respectively.
- Create a counter for both sublists to count the frequencies of each number within each sublist.
- Use a helper function to grab the top two most frequent numbers from each sublist.
- If both sublists have a unique top most frequent number, return the amount of swaps needed for the alternating list to contain an alternation of the top most frequent number for  even and odd elements.
- If both sublists do not have a unique top most frequent number with eachother, return the amount of swaps needed for the alternating list to contain an alternation of the top most frequent number for one sublist, while the other uses the second most frequent number. Both options are calculated, and the minimum is returned.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$