class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        for i in range(len(nums)):
            position = bisect_left(dp, nums[i])
            if position == len(dp):
                dp.append(nums[i])
            else:
                dp[position] = nums[i]
        
        return len(dp)
