# Solution Walk Through
Question: https://leetcode.com/problems/maximum-swap/

## Intuition
I'd first need to get all the digits from `num` using the modulus operator and integer divison, then I can iterate though the digits checking where the best digit to swap (if any) is. Once I have that digit, I can look for the highest digit after it for the swap.

## Approach
- Obtain all the digits from `num` and place them in a list.
- Look through the digits to find the first point where a swap could be needed.
- If a swap is needed, find the highest digit after the first point, as it will be used for the swap.
- Once the highest value digit is found, iterate though digits again to find the first value that can swap with the highest digit.

## Time Complexity
$O(d)$

$d$ is the amount of digits in `num`.

## Space Complexity
$O(d)$