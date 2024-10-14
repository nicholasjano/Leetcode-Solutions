class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        high = len(arr) - 1
        low = 0

        while low <= high:
            mid = (high + low) // 2
            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low + k