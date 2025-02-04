class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
                max_sum = max(max_sum, current_sum)
            else:
                current_sum = nums[i]
        
        return max_sum