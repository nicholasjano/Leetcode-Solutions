class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD_VALUE = 10**9 + 7
        
        if multiplier == 1:
            return [num % MOD_VALUE for num in nums]
        
        if len(nums) == 1:
            nums[0] = ((nums[0] % MOD_VALUE) * pow(multiplier, k, MOD_VALUE)) % MOD_VALUE
            return nums
        
        def multiply_and_update(heap):
            num, index = heap[0]
            new_num = num * multiplier
            heapreplace(heap, (new_num,index))
            nums[index] = new_num
            return new_num

        max_value = max(nums)
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))

        while k > 0:
            new_num = multiply_and_update(heap)
            k -= 1
            
            if new_num > max_value:
                break

        if k > 0:
            quotient = k // len(nums)
            remainder = k % len(nums)
            
            for i in range(len(nums)):
                nums[i] = (nums[i] * pow(multiplier, quotient, MOD_VALUE))
            
            if remainder > 0:
                heap = []
                for i, num in enumerate(nums):
                    heappush(heap, (num, i))
                
                while remainder > 0:
                    multiply_and_update(heap)
                    remainder -= 1
        
        for i in range(len(nums)):
            nums[i] = nums[i] % MOD_VALUE
        
        return nums
