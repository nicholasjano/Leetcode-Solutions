# Solution Walk Through
Question: https://leetcode.com/problems/merge-k-sorted-lists/

## Intuition
I can use a divide and conquer technique to merge lists with eachother in $\log(k)$ time, without needing extra space like a heap. Similar to how a tournament works, each loop, half the lists will get merged with eachother.

## Approach
- Cover the base case when `lists` is empty
- Start with interval = 1, merging adjacent lists (0 with 1, 2 with 3)
- Double the interval each pass, creating progressively larger merged lists
- Continue until all lists are merged into one
- For merging lists, use the same approach as "Merge Two Sorted Lists"


## Time Complexity
$O(n \log k)$

$n$ is the amount of total nodes in `lists`.

## Space Complexity
$O(1)$