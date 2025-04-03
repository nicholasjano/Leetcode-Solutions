# Solution Walk Through
Question: https://leetcode.com/problems/insert-delete-getrandom-o1/

## Intuition
I can create a list to store the values, and a hashmap to map positions of each value on the list. To insert, just append the value onto the list, and map the position of the value onto the hashmap. To remove, I'd need to replace the value with the final value, and pop the not unused last value out. This ensures $O(1)$ complexity. To get a random value, just return a random choice from the values list.

## Approach
- `__init__()`:
    - Initialize a list `self.nums` for the values, and a hashmap `self.pos` for the mapping of values to their positions (indicies on `self.nums`).
- `insert()`:
    - If the value already exists, return False.
    - Otherwise, add the value to `self.nums` and its position mapped on `self.pos` and return True.
- `remove()`:
    - If the value doesn't exist, return False.
    - Otherwise, first check if the value to remove is at the end of `self.nums`. If it is, just remove the value from both `self.nums` and `self.pos` and return True.
    - Otherwise, place the final value from `self.nums` in the position of the value to be removed, and update its new `self.pos` mapping, then delete the removed value from both `self.nums` and `self.pos` and return True.
- `getRandom()`:
    - Return a random value from the list `self.nums` using `Random.choice()`

## Time Complexity
`__init__()`: $O(1)$ \
`insert()`: $O(1)$ \
`remove()`: $O(1)$ \
`getRandom()`: $O(1)$

## Space Complexity
$O(n)$

$n$ represents the amount of total values.