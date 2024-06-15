class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = maximum = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                maximum = max(maximum, current)
                current = 0
        return max(maximum, current)
        