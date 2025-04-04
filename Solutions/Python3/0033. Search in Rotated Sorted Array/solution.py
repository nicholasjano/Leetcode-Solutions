class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            in_left_array = nums[mid] >= nums[0]
            target_in_left = target >= nums[0]
            
            if in_left_array:
                if target_in_left and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if not target_in_left and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1