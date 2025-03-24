class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        curr_index = 0
        for i in range(n):
            if nums[i] != 0:
                nums[curr_index] = nums[i]
                curr_index += 1
        
        for i in range(curr_index, n):
            nums[i] = 0

        return nums