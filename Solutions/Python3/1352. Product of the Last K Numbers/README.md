# Solution Walk Through
Question: https://leetcode.com/problems/product-of-the-last-k-numbers/

## Intuition
I first came up with a solution where I could keep track of the stream, and when `getProduct` was called, I'd multiply the last `k` elements together. This provides the proper output, but the time complexity of $O(k)$ could be improved. I came up with a solution where the prefix product can be stored, and reset at 0. When `getProduct` is called, the current prefix product divided by the first index out of `k` will represent the product up to `k` in $O(1)$ time.

## Approach
- Setup a variable to store the current prefix product, and a list to store the past prefix products.
- add:
    - Multiply the prefix product by `num`, and add value this to the prefix products list. If `num` is 0, reset the prefix products list and current prefix product.
- getProduct:
    - Condition 1: If the length of the past prefix products is less than `k`, that means a 0 has been passed within the last `k` elements, so 0 will be returned.
    - Condition 2: If the length of the past prefix products equals `k`, then just return the current prefix product.
    - Condition 3: If the length of the past prefix products is greater than `k`, then return the current prefix product divided by the first prefix product outside of `k`.

## Time Complexity
$O(1)$

## Space Complexity
$O(n)$

$n$ represents the total number of integers in the stream.