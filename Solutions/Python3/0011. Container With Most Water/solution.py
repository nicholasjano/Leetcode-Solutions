class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        left = 0
        right = n - 1
        while left < right:
            h_left = height[left]
            h_right = height[right]
            min_height = min(h_left, h_right)
            area = min_height * (right - left)
            max_area = max(max_area, area)

            if h_left < h_right:
                left += 1
            else:
                right -= 1
        
        return max_area