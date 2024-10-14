# Solution Walk Through
Question: https://leetcode.com/problems/kth-missing-positive-number/

## Intuition
I can use binary search to find the smallest index where `arr[mid] - (mid + 1) >= k`. If this condition is true, it means the amount of numbers missing from 1 to `arr[mid]` is greater than or equal to `k`. Afterward, we'll have the total number of numbers not missing before that index, and the index of the missing value. Add those two together for the answer.

## Approach
- Create a binary search algorithm.
- If `arr[mid] - (mid + 1) < k`, this means there are not at least `k` missing numbers before the index, so we need to move forward by moving the `low` pointer up.
- If `arr[mid] - (mid + 1) >= k`, this means there are  at least `k` missing numbers before the index, so we need to move backwards by moving the `high` pointer down. This is done to ensure we can find the smallest index where this condition is true.

## Time Complexity
$O(\log n)$

$n$ is the length of `arr`.

## Space Complexity
$O(1)$