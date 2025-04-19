# Solution Walk Through
Question: https://leetcode.com/problems/contains-duplicate-ii/

## Intuition
I can iterate through `nums`, storing each number in a set, and checking if each value already exists in the set. To save space, I can remove any value from the set that will not meet the requirements of `abs(i - j) <= k`, which means the set can hold at most `k + 1` values.

## Approach
- Create a set to store previously visited values.
- Loop through `nums`.
- Within the loop, if `i > k`, remove the least recently added value to the set as it is out of the range for `abs(i - j) <= k` with the current `i`.
- If the current `num` is in the set, return True. Otherwise, add `num` to the set and continue.
- If the loop exits with no match, return False.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(\min(n, k))$