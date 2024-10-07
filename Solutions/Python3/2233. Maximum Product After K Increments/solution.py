class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD_VALUE = 10**9 + 7

        heapify(nums)

        for _ in range(k):
            heapreplace(nums, nums[0] + 1)

        final_product = 1
        for num in nums:
            final_product *= (num % MOD_VALUE)
            final_product %= MOD_VALUE
        
        return final_product
