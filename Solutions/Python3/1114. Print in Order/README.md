# Solution Walk Through
Question: https://leetcode.com/problems/print-in-order/

## Intuition
Use semaphores to block second() and third() from executing at the same time as first(). Once first() is done, the semaphore for second() is released, and once second() is done, the semaphone for third() is released. The with statement will be used as the context manager for each method.

## Approach
- Initialize two semaphores as self.gates[0] and self.gates[1], which are both blocked.
- Run first(), which runs printFirst(), then releases the semaphore at self.gates[0] for second().
- second() runs, which runs printSecond(), then releases the semaphore at self.gates[1] for third().
- third() runs, which runs printThird().

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$