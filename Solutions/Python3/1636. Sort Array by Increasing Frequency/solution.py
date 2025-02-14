class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        nums.sort(key=lambda num: (counts[num], -num))
        return nums