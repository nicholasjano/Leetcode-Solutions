class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        low, high = 2, x
        while low <= high:
            mid = (low + high) // 2
            square_mid = mid*mid
            if square_mid < x:
                low = mid + 1
            elif square_mid > x:
                high = mid - 1
            else:
                return mid
        return high
        