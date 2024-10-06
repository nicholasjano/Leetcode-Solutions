class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        patches = 0
        out_of_range = 1 # current max range = out_of_range - 1
        index = 0

        while (out_of_range - 1) < n:

            if index < len(nums) and nums[index] <= out_of_range:
                out_of_range += nums[index]
                index += 1
            else:
                patches += 1
                out_of_range *= 2
        
        return patches
