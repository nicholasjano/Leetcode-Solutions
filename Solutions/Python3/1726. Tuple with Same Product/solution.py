class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0

        products = {}
        total_tuples = 0
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                if product in products:
                    total_tuples += (products[product] * 8)
                    products[product] += 1
                else:
                    products[product] = 1
        
        return total_tuples
            