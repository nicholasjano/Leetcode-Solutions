# Solution Walk Through
Question: https://leetcode.com/problems/richest-customer-wealth/

## Intuition
Loop through each customer, accumulate their wealth, and check if it is the highest.

## Approach
- Initialize a variable to store the highest wealth value.
- Loop through each person. Within each loop, sum the values of all their accounts.
- Check if their wealth is the new highest wealth value, and set it to the new value if true.

## Time Complexity
$O(n \cdot m)$

## Space Complexity
$O(1)$