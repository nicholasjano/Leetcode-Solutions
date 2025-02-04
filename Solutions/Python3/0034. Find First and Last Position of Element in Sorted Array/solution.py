class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bound_positions = [-1, -1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                bound_positions[0] = mid
                right = mid - 1
        
        if bound_positions[0] == -1:
            return bound_positions
        
        left = bound_positions[0]
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                bound_positions[1] = mid
                left = mid + 1
        
        return bound_positions
