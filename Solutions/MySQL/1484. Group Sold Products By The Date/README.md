# Solution Walk Through
Question: https://leetcode.com/problems/group-sold-products-by-the-date/

## Intuition
I can group by each sell_date, then I can count each distinct product for num_sold, then I can group together all the products for the final string.

## Approach
- Select sell_date from activities .
- Included in the select is a count of all the distinct products for the number of products sold.
- Also included in the select is a concatenation of all the products in lexicographical order seperated by a comma.
- Finally, the resulting table is ordered by sell_date.