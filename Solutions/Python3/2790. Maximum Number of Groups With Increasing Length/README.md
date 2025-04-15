# Solution Walk Through
Question: https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

## Intuition
I first came up with a heap approach, but this was $O(n \log n)$ time, and it could be improved with counting sort. I can count how many times each usage limit occurs, and iterate from 1 to `n`. I can then use a greedy approach, adding each element from lowest usage limit to highest, and creating new groups whenever possible, and keeping track of how many unused numbers are remaining.

## Approach
- Cap each value in `usageLimits` to `n`, as higher values are unnecessary.
- Create a counter dictionary, with the key as a usage limit, and the value as the occurences of that usage limit.
- Loop from 1 to `n` inclusive, representing usage limits from min to max.
- For each loop iteration, get the amount of occurences of that usage limit, and loop for each value.
- For each occurence, add the limit to `total_available`, which represents the total numbers avaliable to form a group.
- If there are enough elements in `total_available` to form a new group, form the group (by incrementing a counter by 1), and substract the amount of used elements from `total_available`.
- Once each occurence has been accounted for, return the groups counter.

## Time Complexity
$O(n)$

$n$ is the length of `usageLimits`.

## Space Complexity
$O(n)$