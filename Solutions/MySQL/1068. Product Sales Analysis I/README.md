# Solution Walk Through
Question: https://leetcode.com/problems/product-sales-analysis-i/

## Intuition
Inner join the tables to get the cooresponding product data for each sale.

## Approach
- Select year, price, and sale_id from the Sales table, as well as the cooresponding product_name
- Inner join with orders, ensuring the proper product_name can be derived for each sale