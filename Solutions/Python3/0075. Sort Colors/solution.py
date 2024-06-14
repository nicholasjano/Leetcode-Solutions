class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_array = [0, 0, 0]
        for num in nums:
            count_array[num] += 1

        current = 0

        for i, num in enumerate(count_array):
            for _ in range(num):
                nums[current] = i
                current += 1