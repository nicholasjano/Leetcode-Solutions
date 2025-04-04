class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        curr = nums[0]
        max_sum = curr
        for i in range(1, n):
            curr = max(nums[i], curr + nums[i])
            max_sum = max(max_sum, curr)
        
        return max_sum
