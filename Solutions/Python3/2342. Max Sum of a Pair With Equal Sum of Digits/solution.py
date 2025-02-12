class Solution:
    def digitSum(self, num: int) -> int:
        result = 0
        while (num != 0):
            result += num % 10
            num //= 10
        return result

    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_values = {}
        max_sum = -1
        for i, num in enumerate(nums):
            curr_digit_sum = self.digitSum(num)
            if curr_digit_sum in digit_sum_values:
                compliment = nums[digit_sum_values[curr_digit_sum]]
                max_sum = max(max_sum, num + compliment)
                if num > compliment:
                    digit_sum_values[curr_digit_sum] = i
            else:
                digit_sum_values[curr_digit_sum] = i
        
        return max_sum
