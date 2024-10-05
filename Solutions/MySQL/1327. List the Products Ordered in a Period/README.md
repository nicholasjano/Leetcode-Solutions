# Solution Walk Through
Question: https://leetcode.com/problems/list-the-products-ordered-in-a-period/

## Intuition
When I see "names of products that have at least 100 units ordered" I know that aggregation would require a having clause. The date constraint would require a where clause. Since I need to select information from two different tables, I'd also need to join the Products and Orders table.

## Approach
- Select product_name from the Products table, as well as the cooresponding sum of units sold
- Inner join with Orders, ensuring the sum of units sold can be calculated
- Include a where clause to contraint only order_date's in February 2020
- Group by product_name to ensure aggregations are calculated based off each product
- Include a having clause to ensure only products with 100+ units ordered are included