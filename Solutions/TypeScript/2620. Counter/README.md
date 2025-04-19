# Solution Walk Through
Question: https://leetcode.com/problems/counter/

## Intuition
TypeScript has closure, which means when a function is returned from another function, it "remembers" the variables from the scope where it was created. In this case, the returned function keeps access to the variable `n`, and can increment it with each call.

## Approach
- Within the `createCounter` function, return a function that when called, returns the increment of `n` as `n++`.

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$