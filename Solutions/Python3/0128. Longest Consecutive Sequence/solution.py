class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        hashmap = {}
        max_sequence_length = 0
        for num in nums:
            left = hashmap.get(num - 1, 0)
            right = hashmap.get(num + 1, 0)
            sequence_length = left + right + 1
            hashmap[num - left] = sequence_length
            hashmap[num + right] = sequence_length
            max_sequence_length = max(max_sequence_length, sequence_length)
        return max_sequence_length