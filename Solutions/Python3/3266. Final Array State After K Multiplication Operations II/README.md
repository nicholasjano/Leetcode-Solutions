# Solution Walk Through
Question: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

## Intuition
I first thought to use a heap and just follow the rules given by the question. Although this works, I was given TLE (Time Limit Exceeded) for large cases. I figured out that if the minimum value is multiplied by the multiplier and becomes the new largest number, this would happen for any remaining values, so I can greedily multiply all the numbers to save time.

Another method to avoid the large number cases is via the forumla: $$(a \cdot b) \mod m = ((a \mod m) \cdot (b \mod m)) \mod m$$
This is benefitial as on the right side of the equation, the mod is calculated on both $a$ and $b$, resulting in smaller and more managable numbers.

## Approach
- Initialize base cases where either multiplier or len(nums) are 1. In these cases, I can skip the heap and finish the question on the spot.
- Create a helper function for future use. This helper function follows the steps in the question by multiplying the minimum number by the multiplier, and pushing it into the heap.
- Now, create the heap with all the numbers in `nums`, paired with their respective indicies for order.
- Looping through k, update the heap each time.
- If the minimum value multiplied never becomes larger than the highest number, then just mod each number by the mod value, and return the list.
- For any minimum value, if the value is multiplied by the multiplier and becomes larger than the initial largest number, we can move over to the greedy approach for the rest of the multiplications.
- For the greedy approach, we calculate a quotient and remainder for the remaining k values. The quotient reprents the amount of full cycles left and we can use to greedily multiply each number. The remainer represents the final few iterations that must be done with the heap. The final remainer iterations will be less than a full cycle. When comeplete, mod each number by the mod value, and return the list.

## Time Complexity
$O(n \log n + k \log n)$

$n$ is the length of `nums`.

## Space Complexity
$O(n)$