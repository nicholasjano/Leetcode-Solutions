class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique_nums = list(count.keys())
        n = len(unique_nums)
        k = n - k

        def quickselect(left, right):
            rand = randint(left, right)
            unique_nums[rand], unique_nums[right] = unique_nums[right], unique_nums[rand]

            pivot = unique_nums[right]
            pointer = left

            for i in range(left, right):
                if count[unique_nums[i]] <= count[pivot]:
                    unique_nums[i], unique_nums[pointer] = unique_nums[pointer], unique_nums[i]
                    pointer += 1
            
            unique_nums[right], unique_nums[pointer] = unique_nums[pointer], unique_nums[right]

            if pointer < k:
                return quickselect(pointer + 1, right)
            
            if pointer > k:
                return quickselect(left, pointer - 1)
            
            return unique_nums[k:]
        
        return quickselect(0, n - 1)