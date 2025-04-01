class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n <= 2:
            return 0
        
        left = 0
        right = n - 1
        max_left = height[left]
        max_right = height[right]
        trapped = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                trapped += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                trapped += max_right - height[right]
        
        return trapped