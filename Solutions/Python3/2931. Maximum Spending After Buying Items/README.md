# Solution Walk Through
Question: https://leetcode.com/problems/maximum-spending-after-buying-items/

## Intuition
Since the day multiplies the price of an item, to get the maximum spending, we need to purchase the most expensive items on the latest days. I can use a minheap to store the values of all possible items we can purchase for the day.

## Approach
- Create the minheap, and push all the values purchasable for the first day. I pop these values out of each shop to make sure I do not purchase duplicate items.
- While loop through the heap, which will end up being m*n time.
- Within each iteration of the loop, I pop the cheapest item from the heap. With that, I add the item value * day to the total spending, and add the next item in that shop to the heap if necessary. The day increments at the end of the loop to ensure proper calculations.

## Time Complexity
$O((mn)log(mn))$

## Space Complexity
$O(m)$