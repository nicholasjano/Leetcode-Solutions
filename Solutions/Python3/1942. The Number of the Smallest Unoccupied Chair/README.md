# Solution Walk Through
Question: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

## Intuition
I initally came up with a brute force solution that utilized a hashmap to store chairs, but this was not efficient. I eventually came to the solution of utilizing 2 heaps, one for to store a pair of each persons (leaving time, occupied chair), and one with the avaliable chairs left. For each persons arrival, I unoccupy any seat for people leaving, and occupy the lowest seat avaliable.

## Approach
- Sort `times` based off arrival.
- Create two heaps, one to store each persons (leaving time, occupied chair) pair, and one for any avaliable seats.
- Loop through times. A base case to check if the arrival time is greater than the target arrival time is done, as any person that meets these condition is irrelevant to the solution.
- For each new person, remove any person that has or is leaving from the persons heap, and add their seat back to occupiable seats. Afterward, occupy the lowest seat avaliable for that person.
- Keep looping until the target person arrives, and return the lowest seat avaliable.


## Time Complexity
$O(n \log n)$

$n$ is the length of `times`.

## Space Complexity
$O(n)$