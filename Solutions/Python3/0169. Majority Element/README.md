# Solution Walk Through
Question: https://leetcode.com/problems/majority-element/

## Intuition
I first came up with a hashmap solution to keep count of each numbers occurences, and to return the value once the occurences were greater than `n / 2`. To optimize the solution, I used Boyer-Moore Voting Algorithm. This algorithm works for this problem because when keeping track of each candidate, by the end, the element with the the majority frequency will always be the candidate. The count ensures that if there is an element with an occurence greater than `n / 2`, the other values will never be able to take candidacy by the end.

## Approach
- Create two variables, one to store the current count of the candidate, and one to store the current candidate number.
- For each number, if the count is 0 (which it will be by default), update the candidate to the current number.
- If the current number is the candidate, increment the count by 1, otherwise, decrement the count by 1.
- By the end, if an element is the majority, either it will be the candidate and other values will not have enough occurences to decrement the count, or it will surpass the count and set itself as the candidate, so the candidate can be returned.

## Time Complexity
$O(n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$