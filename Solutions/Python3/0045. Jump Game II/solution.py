class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        left = 0
        right = 0
        jumps = 0
        while right < n - 1:
            max_jump = 0
            for i in range(left, right + 1):
                max_jump = max(max_jump, nums[i] + i)
            
            left, right = right + 1, max_jump
            jumps += 1
        
        return jumps