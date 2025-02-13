class Solution:
    def minOperations(self, nums: List[int], k: int) -> int: 
        heapify(nums)
        operations = 0
        while len(nums) >= 2:
            x = heappop(nums)
            y = heappop(nums)

            if x >= k:
                return operations
            
            heappush(nums, x*2 + y)
            operations += 1
        
        return operations
