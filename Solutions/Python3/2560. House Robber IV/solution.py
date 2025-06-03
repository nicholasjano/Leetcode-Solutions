class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 1
        right = max(nums)
        min_steal = right
        while left <= right:
            steal_amount = (left + right) // 2

            index = 0
            possible_thefts = 0
            while index < n:
                if nums[index] <= steal_amount:
                    possible_thefts += 1
                    index += 2
                else:
                    index += 1
            
            if possible_thefts >= k:
                min_steal = steal_amount
                right = steal_amount - 1
            else:
                left = steal_amount + 1
        
        return min_steal
