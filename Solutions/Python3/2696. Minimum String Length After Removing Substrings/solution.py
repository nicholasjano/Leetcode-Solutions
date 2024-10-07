class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
                continue
            
            left_value = ord(stack[-1]) - 65
            right_value = ord(char) - 66
            if right_value == left_value and left_value <= 2 and left_value % 2 == 0:
                stack.pop()
            else:
                stack.append(char)

        return len(stack)