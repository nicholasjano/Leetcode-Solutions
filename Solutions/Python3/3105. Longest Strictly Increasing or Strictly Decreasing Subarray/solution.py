class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_count = 1
        max_increasing_count = 1
        decreasing_count = 1
        max_decreasing_count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increasing_count += 1
                max_increasing_count = max(max_increasing_count, increasing_count)
                decreasing_count = 1
            elif nums[i] < nums[i-1]:
                decreasing_count += 1
                max_decreasing_count = max(max_decreasing_count, decreasing_count)
                increasing_count = 1
            else:
                increasing_count = 1
                decreasing_count = 1
        
        return max(max_increasing_count, max_decreasing_count)