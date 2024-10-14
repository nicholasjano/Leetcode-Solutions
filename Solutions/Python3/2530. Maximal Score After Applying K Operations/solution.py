class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num
        
        heapify(nums)

        score = 0
        for _ in range(k):
            max_val = -(nums[0])
            score += max_val
            replacement = -(ceil(max_val / 3))
            heapreplace(nums, replacement)
        
        return score