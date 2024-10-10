class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        h1, h2, h3 = nums[0], nums[1], nums[2] + nums[0]
        for i in range(3, n):
            h3, h2, h1 = max(nums[i] + h2, nums[i] + h1), h3, h2
        
        return max(h3, h2)
