# Solution Walk Through
Question: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

## Intuition
I can sort the jobs my parting time, and create a triplet for each job. I first came up with a recursive backtracking solution with memoization, but this was not efficient enough. I came up with a bottom up DP approach where the DP arrat stores the maximum profit from each job forward, where the loop starts at the latest starting time job and moves bakcwards. The key for efficiency is to use binary search to find the next avaliable job from a certain job.

## Approach
- Create a new list `jobs` that stores each job as a triplet, and is sorted in ascending order of `startTime`.
- Initialize a DP array of size `n`, representing the maximum profit from each index.
- Initialize a list containing all the start times in order, for use in binary search.
- Loop in reverse, starting from the latest starting job. Grab the start, end, and profit values for that job.
- Use binary search on the start times to find the next possible job when including the current job. If it exists, add its profit to the current profit.
- Set the value for the DP array at the current index to the maximum profit from that index, which is either the current profit, or the profit from the next index.
- Once the loop is complete, the result will be the maximum profit from the very beginning, so the profit from the first index of the DP list can be returned.

## Time Complexity
$O(n \log n)$

$n$ is the length of `startTime`.

## Space Complexity
$O(n)$