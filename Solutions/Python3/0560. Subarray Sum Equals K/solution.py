class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        total_subarrays = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            difference = prefix_sum - k
            if difference in prefix_sums:
                total_subarrays += prefix_sums[difference]
            
            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
            
        return total_subarrays