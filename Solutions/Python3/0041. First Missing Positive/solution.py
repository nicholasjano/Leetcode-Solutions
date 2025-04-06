class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            correct_index = num - 1
            if 0 < num <= n and nums[i] != nums[correct_index]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        
        return n + 1
