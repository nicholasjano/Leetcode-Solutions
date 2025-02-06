# Solution Walk Through
Question: https://leetcode.com/problems/tuple-with-same-product/

## Intuition
This question has fimiliarity to two sum, where I have to find the compliment (in this case, two sets of numbers that have the same product). I can store all the products of number pairs, and if I find two different numbers that match a saved product, I know I have a unique set of numbers that have equal products, and they can be arranged in 8 ways, as shown in the example.

## Approach
- Base case for `n < 4` as you need 4 numbers for this question
- Loop through each number pair in `nums` and store their product in a hashmap
- If their products have been seen before, increment `8 * the amount of times that product has been stored prior` to the result variable
- Return the result variable

## Time Complexity
$O(n^2)$

$n$ is the length of `nums`.

## Space Complexity
$O(n^2)$