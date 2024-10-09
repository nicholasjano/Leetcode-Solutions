class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        step1, step2 = 1, 2
        for _ in range(2, n):
            step1, step2 = step2, step1 + step2
        
        return step2