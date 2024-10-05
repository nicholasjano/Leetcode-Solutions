class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        t1, t2, t3 = 0, 1, 1
        for _ in range(n-2):
            t1, t2, t3 = t2, t3, t3 + t2 + t1
        
        return t3