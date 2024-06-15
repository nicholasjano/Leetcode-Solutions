# Solution Walk Through
Question: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

## Intuition
Sort the plants by growth time as that is a bottleneck, plant each flower one at a time, in order descending order of growth time.

## Approach
- Create a list to pair each plant with their plant time and growth time.
- Sort the list based off growth time, so the highest growth time plants can be planted first.
- For each loop iteration, remove the last index of the list.
- Add the plant time to days, and both times to minimum total days
- With each plant, ensure minimum total days never decreases, so keep the minimum total days of the bottlenecking plant that takes the longest.
- Once all plants have been accounted for, return minimum total days

## Time Complexity
$O(n \log n)$

## Space Complexity
$O(n)$