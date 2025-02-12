# Solution Walk Through
Question: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

## Intuition
I can store each digit sum for each number in a hashmap, and if another number has the same digit sum, I can sum them and see if it's the new highest sum. If 3 numbers have the same digit sum, just use the top two.

## Approach
- Create a hash map to store digit sums
- Loop through `nums` and for each number, check if it's digit sum has been visited prior
- If it has not, add it to the hashmap and continue
- If it has been visited, sum the two values, and store the sum as the max sum if applicable. Also ensure that the hashmap only stores the highest value each digit sum to ensure the max sum won't be missed.
- Once the loop is done, return the max sum

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$