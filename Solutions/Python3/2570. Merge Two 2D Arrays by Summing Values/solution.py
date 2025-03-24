class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        nums1_index = 0
        nums2_index = 0
        while nums1_index < len(nums1) and nums2_index < len(nums2):
            nums1_id = nums1[nums1_index][0]
            nums2_id = nums2[nums2_index][0]

            if nums1_id < nums2_id:
                result.append(nums1[nums1_index])
                nums1_index += 1
            elif nums2_id < nums1_id:
                result.append(nums2[nums2_index])
                nums2_index += 1
            else:
                nums_sum = nums1[nums1_index][1] + nums2[nums2_index][1]
                result.append([nums1_id, nums_sum])
                nums1_index += 1
                nums2_index += 1
        
        while nums1_index < len(nums1):
            result.append(nums1[nums1_index])
            nums1_index += 1
        
        while nums2_index < len(nums2):
            result.append(nums2[nums2_index])
            nums2_index += 1
        
        return result