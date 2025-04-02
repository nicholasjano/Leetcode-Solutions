# Solution Walk Through
Question: https://leetcode.com/problems/top-k-frequent-elements/

## Intuition
My first though was to use a maxheap, but the solution can be more optimal. A variation of bucket sort can be used to store the numbers in `nums` in order of their occurences. This way, to get the k largest, I can just navigate the list until I reach k.

## Approach
- Store the occurences of each number in `nums` in a hashmap.
- Create a 2D list with a size of the number with the highest occurences.
- For each number, occurences pair from the hashmap, place the number with the index of the occurence.
- Loop the 2D list backwards to grab the top k elements.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$