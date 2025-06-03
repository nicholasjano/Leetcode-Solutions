class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        max_candies = 0
        while left <= right:
            candy_amount = (left + right) // 2

            max_k = 0
            for pile in candies:
                max_k += (pile // candy_amount)
            
            if max_k >= k:
                max_candies = candy_amount
                left = candy_amount + 1
            else:
                right = candy_amount - 1
        
        return max_candies
