# Solution Walk Through
Question: https://leetcode.com/problems/top-k-frequent-elements/

## Intuition
I can use quickselect to find the `k`th top frequent element. I can first get the counts of each number from `nums`, then create a list of all the unique numbers. This unique numbers list and their respective frequency counts will be used for the quicksort.

## Approach
- Change `k` to be the index where the `k`th largest value is.
- Get the count of each number from `nums`. The keys will be the unique values from `nums`.
- Start Quickselect with all of the unique numbers.
- Pick a random index as the pivot, and swap it to the right.
- Set the pointer to be the leftmost value.
- For every other number in `nums`, if the frequency is less than the pivots frequency, swap it with the most recent pointer value, and increment the pointer. This will ensure numbers with less frequency then the pivot get swapped behind numbers with a higher frequency than the pivot.
- At the end, swap the pivot with the current pointer. This will ensure all numbers on the left of the pivot have a smaller frequency than or equal to the pivot, and all the number on the right all have larger frequencies than the pivot.
- If the pointer is less than `k`, that means the result is on the right partition, so rerun quicksort with this partition.
- If the pointer is greater than `k`, that means the result is on the left partition, so rerun quicksort with this partition.
- If the pointer equals `k`, the correct partition is found, and return the unique numbers list from `k`.

## Time Complexity
$O(n)$

$n$ is the length of `nums`. \

Note: In rare worst-care, the time complexity could be $O(n^{2})$

## Space Complexity
$O(n)$