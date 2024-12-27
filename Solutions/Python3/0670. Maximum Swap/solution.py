class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        
        digits = digits[::-1]
        
        swap_needed = False
        start_index = -1
        for i in range(len(digits) - 1):
            if digits[i] < digits[i+1]:
                swap_needed = True
                start_index = i
                break
        
        if swap_needed:
            highest_index = start_index
            for i in range(start_index + 1, len(digits)):
                if digits[i] >= digits[highest_index]:
                    highest_index = i
            
            for i in range(start_index + 1):
                if digits[i] < digits[highest_index]:
                    digits[i], digits[highest_index] = digits[highest_index], digits[i]
                    break

        
        final_num = 0
        for digit in digits:
            final_num = final_num * 10 + digit
        
        return final_num