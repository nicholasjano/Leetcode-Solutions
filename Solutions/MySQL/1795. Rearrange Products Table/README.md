# Solution Walk Through
Question: https://leetcode.com/problems/rearrange-products-table/

## Intuition
Since there are only 3 stores, I can select the proper (product_id, store, price) combination for each store, and union the results.

## Approach
- For each store, select the product_id, name (as a string), and price from products.
- Include a where clause to make sure that for that product, the respective store is not null. This ensures that the product is avaliable in the store.
- Union all the results together.