class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            if num % 3 != 0:
                total += 1
        return total