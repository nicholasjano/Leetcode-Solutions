class Solution:
    def findLeftmostPos(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
    def findRightmostPos(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left

    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        
        for num in candidates:
            left = self.findLeftmostPos(arr, num)
            right = self.findRightmostPos(arr, num)
            if right - left > n // 4:
                return num
