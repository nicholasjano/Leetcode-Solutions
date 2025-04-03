class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        min_reachable = n - 1

        for i in range(n - 2, -1, -1):
            num = nums[i]
            max_jump = i + num
            if max_jump >= min_reachable:
                min_reachable = i
        
        return min_reachable == 0