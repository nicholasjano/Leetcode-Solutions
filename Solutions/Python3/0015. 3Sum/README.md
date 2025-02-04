# Solution Walk Through
Question: https://leetcode.com/problems/3sum/

## Intuition
I first tried a solution using a hashmap to store all sums between two numbers, and see which third number compliments, similar to two sum, but this method was inefficient. What I ended up figuring out was if I sort the list, then loop though each number in `nums` as if it was the first number in a triplet, I can use a two pointer approach to figure potential matched for the triplet. I can skip duplicates to ensure the result list only has distinct triplets.

## Approach
- Sort `nums`
- Loop though each number in `nums`
- Base case for each loop will skip a number if the previous is a duplicate to ensure distinct triplets
- Use a two pointer approach starting from left (right after the current number) and right (the end of the list)
- If the sum of the current number, left, and right is less than 0, move left up
- If the sum is greater than 0, move right down
- If the sum is 0, add the triplet to `result`, skip past duplicates for left and right, move to the next values for both, and continue
- Once all numbers have been looped through, return `result`

## Time Complexity
$O(n^2)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$