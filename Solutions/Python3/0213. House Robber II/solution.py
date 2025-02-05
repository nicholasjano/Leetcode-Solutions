class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(houses):
            n = len(houses)

            if n <= 2:
                return max(houses)

            h1, h2, h3 = houses[0], houses[1], houses[2] + houses[0]
            for i in range(3, n):
                h3, h2, h1 = max(houses[i] + h2, houses[i] + h1), h3, h2
            
            return max(h3, h2)
        
        n = len(nums)

        if n <= 3:
            return max(nums)

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))
