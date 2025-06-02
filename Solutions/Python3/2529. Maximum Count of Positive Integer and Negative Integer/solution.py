class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1
        rightmost_negative = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                rightmost_negative = mid
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = n - 1
        leftmost_positive = n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                leftmost_positive = mid
                right = mid - 1
            else:
                left = mid + 1

        return max(rightmost_negative + 1, n - leftmost_positive)
