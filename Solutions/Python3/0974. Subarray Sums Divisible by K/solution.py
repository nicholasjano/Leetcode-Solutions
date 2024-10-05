class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subarrays = 0
        hashmap = {0: 1}
        sum = 0

        for num in nums:
            sum += num
            rem = sum % k
            if rem in hashmap:
                subarrays += hashmap[rem]
                hashmap[rem] += 1
            else:
                hashmap[rem] = 1
            
        return subarrays
        