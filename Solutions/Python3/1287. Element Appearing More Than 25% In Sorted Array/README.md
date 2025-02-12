# Solution Walk Through
Question: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

## Intuition
First I had the idea to use a counter hashmap to store occurences, but since the list is sorted, I knew I could use binary search to help. Since I'm looking for the element with over 25% occurence, I can set points at the 25% mark, 50% mark, and 75% mark, and I'll know at one of those numbers is the target. To figure out which one, I can run binary search on all 3 to find the total occurences, and see if it suprasses the target.

## Approach
- Create a list of candidate numbers at the 25% mark, 50% mark, and 75% mark of `arr`
- For each, find the leftmost insert position and rightmost insert position using binary search
- If the difference in insert positions (also equal to occurences) is above 25% of the length of `arr`, return it

## Time Complexity
$O(\log n)$

$n$ is the length of `arr`.

## Space Complexity
$O(1)$