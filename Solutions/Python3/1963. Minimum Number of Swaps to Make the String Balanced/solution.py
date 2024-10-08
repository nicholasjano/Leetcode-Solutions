class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        movement_direction = 1 # left = 0 right = 1
        swaps = 0
        balance = 0
        while left <= right:
            if movement_direction == 1:
                char = s[left]
                if char == "[":
                    balance += 1
                else:
                    balance -= 1
                    if balance < 0:
                        swaps += 1
                        movement_direction = 0
                left += 1
            else:
                char = s[right]
                if char == "[":
                    balance += 2
                    movement_direction = 1
                
                right -= 1

        return swaps