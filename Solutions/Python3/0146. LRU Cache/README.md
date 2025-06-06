# Solution Walk Through
Question: https://leetcode.com/problems/lru-cache/

## Intuition
I can store the nodes in a hashmap, with the key as the `key` parameter. Whenever a `put()` is ran, either move the existing node to the end with the new `value`, or create a new node and place it at the end. When `get()` is ran, move the existing node to the end, if it exists. If the capacity becomes too large, remove the node at the head.

## Approach
- `__init__()`:
    - Set up a doubly linked list to store the key, value pairs.
    - Initalize the cache, and set the head/tail of the doubly linked list to dummy values to prevent NoneType errors.
- `get()`:
    - If the key already exists, remove the node from the linked list, and add it to the end, and return the value. Otherwise return -1.
- `put()`:
    - If the key already exists, remove the node from the linked list, and add it to the end. Otherwise, just add the new node to the end with the value. If the length now surpasses the capacity, remove the node at the head (least recently used).
- `add()`:
    - Add a node to the front of the linked list.
- `remove()`:
    - Remove a node to the front of the linked list.

## Time Complexity
`__init__()`: $O(1)$ \
`get()`: $O(1)$ \
`put()`: $O(1)$ \
`add()`: $O(1)$ \
`remove()`: $O(1)$

## Space Complexity
$O(n)$

$n$ is the value of `capacity`.