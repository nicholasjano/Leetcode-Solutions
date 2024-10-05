# Solution Walk Through
Question: https://leetcode.com/problems/n-th-tribonacci-number/

## Intuition
I can use bottom-up dynamic programming to work my way up to n, using three variables representing $T(n - 3)$, $T(n - 2)$, and $T(n - 1)$ respectively. I could also use recursion with memoization, but that would use more space.

## Approach
- Cover base cases for n = 0 and n <= 2
- Set the variables t1, t2, and t3, representing $T(n - 3)$, $T(n - 2)$ and $T(n - 1)$ respectively
- Loop to n-2, where on each loop, sum t1, t2, and t3 for the currrent value, and move the value from t3 to t2 and value from t2 to t1.
- Since the loop runs n-2 times, t3 will end up being the result when the loop is done.

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$