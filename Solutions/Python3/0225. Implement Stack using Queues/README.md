# Solution Walk Through
Question: https://leetcode.com/problems/implement-stack-using-queues/

## Intuition
I can use one queue, keeping the most recent value at the front of the queue by reappending every other value value to the back.

## Approach
- `__init__()`:
    - Initalize the queue.
- `push()`:
    - Append `x` to the back of the queue, and then reappend every other value to the back of the queue.
- `pop()`:
    - Pop from the front of the queue.
- `top()`:
    - Peek from the front of the queue.
- `empty()`:
    - Check if the queue is empty.

## Time Complexity
`__init__()`: $O(1)$ \
`push()`: $O(1)$ \
`pop()`: $O(n)$ \
`top()`: $O(1)$ \
`empty()`: $O(1)$

$n$ is the number of elements in the stack.

## Space Complexity
$O(n)$