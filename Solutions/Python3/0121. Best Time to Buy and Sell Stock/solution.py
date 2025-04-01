class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_smallest = prices[0]
        curr_largest = prices[0]
        max_gap = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price < curr_smallest:
                curr_smallest = price
                curr_largest = price
            
            if price > curr_largest:
                curr_largest = price
            
            max_gap = max(max_gap, curr_largest - curr_smallest)
        
        return max_gap