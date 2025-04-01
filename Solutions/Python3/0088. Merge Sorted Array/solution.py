class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_position = m - 1
        nums2_position =  n - 1
        index = m + n - 1
        while index >= 0:
            if nums1_position < 0:
                nums1[index] = nums2[nums2_position]
                nums2_position -= 1
            elif nums2_position < 0:
                nums1[nums1_position], nums1[index] = nums1[index], nums1[nums1_position]
                nums1_position -= 1
            elif nums1[nums1_position] > nums2[nums2_position]:
                nums1[nums1_position], nums1[index] = nums1[index], nums1[nums1_position]
                nums1_position -= 1
            else:
                nums1[index] = nums2[nums2_position]
                nums2_position -= 1
            index -= 1
