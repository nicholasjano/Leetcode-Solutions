# Solution Walk Through
Question: https://leetcode.com/problems/count-number-of-bad-pairs/

## Intuition
I can count the total number of good pairs and subtract it from the total number of pairs to get all the bad pairs. I can count the amount of times `nums[i] - i` has been occured to see how many good pairs any number has.

## Approach
- Set up the total pairs to be `(n * (n - 1)) // 2`
- Loop through `nums` and check how many times `num - i` has already occured, and add it to the good pairs accumulator
- Ensure `num - i` is incremented by 1 in the counter hashmap for future pairs
- Once the loop is complete, return the total pairs - the good pairs counts

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$