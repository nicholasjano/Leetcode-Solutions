# Solution Walk Through
Question: https://leetcode.com/problems/lfu-cache/

## Intuition
I can create two hashmaps. The first one will store the cache with the inputted key, value pairs, along with the current frequency of the key. The second will have each frequency value (1, 2, 3, ...) as the key, and an ordered dictionary as the value. When a value needs to be removed, the first item added to the lowest frequency hashamp will be removed.

## Approach
- `__init__()`:
    - Initialize `self.cache` to store the key, value pairs along with the current frequency of the key.
    - Initialize `self.frequencies` to store buckets of each frequency, holding the keys.
- `get()`:
    - If the key is not in `self.cache`, return -1.
    - If the key does exist, increment its frequency by 1, and move it to the next frequency bucket. If the previous frequency bucket is empty and it was the minimum frequency, move the minimum frequency up one.
    - Return the key's value from `self.cache`.
- `put()`:
    - If the key exists in `self.cache`, update its value and increment its frequency by 1, and move it to the next frequency bucket. If the previous frequency bucket is empty and it was the minimum frequency, move the minimum frequency up one.
    - If the key is not in `self.cache`, first check if the capacity would be overflow.
    - If the capacity would overflow, delete the key that was least recently used from the minimum frequency bucket.
    - Afterward, add the new key, frequency pair (frequency would be 1) to the cache and frequency bucket.

## Time Complexity
`__init__()`: $O(1)$ \
`get()`: $O(1)$ \
`put()`: $O(1)$

## Space Complexity
$O(n)$

$n$ is the value of `capacity`.