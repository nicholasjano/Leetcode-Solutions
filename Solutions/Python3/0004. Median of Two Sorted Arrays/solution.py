class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = total // 2

        large, small = (nums1, nums2) if m > n else (nums2, nums1)

        left = 0
        right = len(small) - 1
        while True:
            mid = (left + right) // 2
            complement = (half - 1) - (mid + 1)

            small_value = small[mid] if mid >= 0 else float("-inf")
            small_next = small[mid + 1] if mid + 1 < len(small) else float("inf")
            large_value = large[complement] if complement >= 0 else float("-inf")
            large_next = large[complement + 1] if complement + 1 < len(large) else float("inf")

            if small_value <= large_next and large_value <= small_next:
                if total % 2 == 0:
                    return (max(small_value, large_value) + min(small_next, large_next)) / 2
                return min(small_next, large_next)
            elif small_value > large_next:
                right = mid - 1
            else:
                left = mid + 1
