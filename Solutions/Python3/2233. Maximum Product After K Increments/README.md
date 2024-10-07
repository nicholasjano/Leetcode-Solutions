# Solution Walk Through
Question: https://leetcode.com/problems/maximum-product-after-k-increments/

## Intuition
Using a greedy approach, I know that the maximum product can be made by incrementing the smallest number each time. I can use a heap to determine the smallest number at each step. Afterward, I need to find the product of `nums` modulo $10^9 + 7$. I can do that, and avoid any large numbers along the way by:

- Calculating `nums[i]` modulo $10^9 + 7$ for each num.
- For each step of calculating the final product, also calculate the current final product modulo $10^9 + 7$.

This keeps all the values in `nums` and the final product underneath $10^9 + 7$, and will still work due to the distributive property of modular arithmetic over multiplication:

$$(a \cdot b) \mod m = ((a \mod m) \cdot (b \mod m)) \mod m$$

## Approach
- Convert `nums` into a heap.
- For `k` times, increment the current lowest value by one, and update the heap.
- Once complete, calculate the final product modulo $10^9 + 7$. The values of `nums[i]` and the running values of `final_product` are also ran modulo $10^9 + 7$ to ensure the values don't get too large.

## Time Complexity
$O(n + k \log n)$

$n$ is the length of `nums`.

## Space Complexity
$O(1)$