class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_indexed = [val for i, val in enumerate(nums) if i % 2 == 0]
        odd_indexed = [val for i, val in enumerate(nums) if i % 2 == 1]
        even_indexed.sort()
        odd_indexed.sort(reverse = True)
        original_len = len(nums)
        nums = []
        for i in range(original_len//2):
            nums.append(even_indexed[i])
            nums.append(odd_indexed[i])

        if original_len % 2 == 1:
            nums.append(even_indexed[-1])
        
        return nums