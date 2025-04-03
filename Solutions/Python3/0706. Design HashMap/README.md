# Solution Walk Through
Question: https://leetcode.com/problems/design-hashmap/

## Intuition
I can create a list of buckets that will scale based off the currest size of the hashmap. In the case of collisions, linkedlist chaining will be used.

## Approach
- `__init__()`:
    - Initialize the buckets list, along with other variables to assist the bucket in resizing.
- `_hash()`:
    - Provide the hashkey.
- `_resize()`:
    - Double the size of the buckets list, and replace each value into the new bucket list.
- `put()`:
    - If the bucket at the hashed index is empty, place the node and resize if needed.
    - Otherwise, nagivate to the end of the chained linkedlist and place the node at the end. If the key is reached beforehand, update the value.
- `get()`:
    - Obtain the hashed index, and navigate the chained linkedlist from the bucket at the hashed inted until the key is found. If the key is not found, return -1.
- `remove()`:
    - Obtain the hashed index. If the hashed index is empty, exit.
    - Otherwise, naviagte the chained linkedlist until the key is found. If it is, remove the node by making the previous node point to the removed nodes next node, ultimately deleting the node to remove.

## Time Complexity
`__init__()`: Average: $O(1)$  Worst: $O(1)$ \
`_hash()`: Average: $O(1)$  Worst: $O(1)$ \
`_resize()`: Average: $O(n)$  Worst: $O(n)$\
`put()`: Average: $O(1)$  Worst: $O(n)$ \
`get()`: Average: $O(1)$  Worst: $O(n)$ \
`remove()`: Average: $O(1)$  Worst: $O(n)$

## Space Complexity
$O(n)$

$n$ represents the amount of key-value pairs.