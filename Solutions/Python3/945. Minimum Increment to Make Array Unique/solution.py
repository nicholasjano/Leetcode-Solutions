class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_num = max(nums)
        count = [0] * (max_num + len(nums))

        for num in nums:
            count[num] += 1
        
        picks = 0
        
        for i in range(len(count)):
            if count[i] > 1:
                excess = count[i] - 1
                picks += excess
                count[i + 1] += excess
                count[i] = 1
        
        return picks