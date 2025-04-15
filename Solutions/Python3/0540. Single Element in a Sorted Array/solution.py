class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            mid_left = mid - 1
            mid_right = mid + 1

            if mid_left < 0 and mid_right >= n:
                return nums[mid]
            
            if mid_left < 0:
                if nums[mid_right] != nums[mid]:
                    return nums[mid]
                left = mid + 1
                continue
            
            if mid_right >= n:
                if nums[mid_left] != nums[mid]:
                    return nums[mid]
                right = mid - 1
                continue
            
            if nums[mid] == nums[mid_left]:
                count_nums_right = n - mid - 1
                if count_nums_right % 2 == 0:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] == nums[mid_right]:
                count_nums_left = mid
                if count_nums_left % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return nums[mid]
