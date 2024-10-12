class Solution:
    def integerBreak(self, n: int) -> int:
        max_product = 1

        for divisor in range(2, n + 1):
            current_value = n//divisor
            remainder = n % divisor
            current_product = 1
            current_product *= current_value ** (divisor - remainder)
            current_product *= (current_value + 1) ** remainder
            max_product = max(max_product, current_product)
        return max_product
        