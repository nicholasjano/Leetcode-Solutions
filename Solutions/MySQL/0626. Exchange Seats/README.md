# Solution Walk Through
Question: https://leetcode.com/problems/exchange-seats/

## Intuition
Create a case clause to determine whether the student should move up a seat, down a seat, or stay the same. This can be done using the modulo operator for even or odd seats.

## Approach
- Create a case clause to swap seats.
- In the first condition, I check whether the student id is the final student, and the table is odd. In this case, they do not change seats.
- In the second condition, I check whether the student id is odd numbered, moving them up a seat.
- Finally, I check whether the student id is even numberes, and moving them down a seat, finishing the swap.