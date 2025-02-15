class Solution:
    def canBePartitioned(self, n: int, target: int) -> bool:
        if target < 0 or n < target:
            return False

        if n == target:
            return True

        divisor = 10
        while n // divisor > 0:
            if self.canBePartitioned(n // divisor, target - (n % divisor)):
                return True
            divisor *= 10

        return False

    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            square = i*i
            if self.canBePartitioned(square, i):
                result += square
        return result
