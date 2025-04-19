class Solution:
    def triangularSum(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        
        times_element_appears = 1
        result = (nums[0] * times_element_appears) % 10
        
        for i in range(1, n):
            positions_remaining = n - i
            current_position = i
            
            times_element_appears = times_element_appears * positions_remaining // current_position
            
            result = (result + nums[i] * times_element_appears) % 10
        
        return result