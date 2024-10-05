# Solution Walk Through
Question: https://leetcode.com/problems/fibonacci-number/

## Intuition
I can use bottom-up dynamic programming to work my way up to n, using two variables representing $F(n - 2)$ and $F(n - 1)$ respectively. I could also use recursion with memoization, but that would use more space.

## Approach
- Cover base cases for n = 0 and n = 1
- Set the variables f1 and f2, representing $F(n - 2)$ and $F(n - 1)$ respectively
- Loop to n-1, where on each loop, sum f1 and f2 for the currrent value, and move the value from f2 to f1.
- Since the loop runs n-1 times, f2 will end up being the result when the loop is done.

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$