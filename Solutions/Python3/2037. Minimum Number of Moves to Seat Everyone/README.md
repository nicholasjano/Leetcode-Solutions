# Solution Walk Through
Question: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

## Intuition
Although I tried to look for more clever solutions, the best way to solve this problem required sorting of both `seats` and `students`. Afterward, you can loop though the lists, summing the difference between the student and the seat at the same index, which is the amount of moves the student needs to get to the seat. The sort will make it so the $i^{th}$ seat will be the most optimal seat for the $i^{th}$ student.

## Approach
- Sort both students and seats.
- Loop through the lists, summing the differences between the student and seat values, which will result in the minimum amount of moves required to seat every student.

## Time Complexity
$O(n \log n)$

## Space Complexity
$O(n)$