# Solution Walk Through
Question: https://leetcode.com/problems/merge-intervals/

## Intuition
I can first sort the intervals, then check if each interval is either mergable or not with the current final interval. If it is mergable, edit the current final interval by updating the range if necessary. If they are not mergable, just add a new interval to the result.

## Approach
- Sort `intervals`.
- Create a result list and store the first interval.
- Loop through the rest of the intervals. For each interval, check if it is mergable by comparing the first number of the interval to the last number of the last interval in the result list.
- If it is mergable, update the last interval in the result lists second value to be the max of that value or the new intervals second value.
- If it is not mergable, append the interval to the result list and continue.
- Once done, return the result list.

## Time Complexity
$O(n \log n)$

$n$ is the length of `intervals`.

## Space Complexity
$O(n)$