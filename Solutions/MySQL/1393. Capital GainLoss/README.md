# Solution Walk Through
Question: https://leetcode.com/problems/capital-gainloss/

## Intuition
Group by each stock, then use an if statement where "Buy" is a negative cost to the overall stock gain/loss, and "Sell" is a positive addition to the overall stock gain/loss.

## Approach
- Select stock_name from stocks 
- Included in the select, have an if statement, where if operation = 'Sell', then add that price, otherwise (if "Buy"), decrement that price, and sum all buy/sell for the overall stock gain/loss.
- Group by stock_name to ensure the overall stock gain/loss are seperate for each stock.