class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k
        def quick_select(left, right):
            rand = randint(left, right)
            nums[rand], nums[right] = nums[right], nums[rand]
            
            pivot = nums[right]
            pointer = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            
            nums[right], nums[pointer] = nums[pointer], nums[right]

            if pointer < k:
                return quick_select(pointer + 1, right)
            
            if pointer > k:
                return quick_select(left, pointer - 1)
            
            return nums[pointer]
        
        return quick_select(0, n - 1)