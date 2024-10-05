# Solution Walk Through
Question: https://leetcode.com/problems/recyclable-and-low-fat-products/

## Intuition
Pretty simple solution, just use a where clause to see if a product is both low fat and recyclable.

## Approach
- Select product_id from Products
- Use a where clause to check if both low_fats and recyclable both equal "y"