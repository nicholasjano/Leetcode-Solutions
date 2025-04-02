class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        result = 0
        max_val = 2**31 - 1

        while x > 0:
            last_digit = x % 10
            x //= 10
            result *= 10
            result += last_digit

            if result > max_val:
                return 0

        if negative:
            result = -result

        return result
