class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if hm.get(compliment) is not None:
                return [hm.get(compliment), i]
            
            hm[num] = i