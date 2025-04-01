class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 2:
                second_most_recent = stack[-2]
                if (
                    (second_most_recent == "(" and char == ")") or
                    (second_most_recent == "{" and char == "}") or
                    (second_most_recent == "[" and char == "]")
                ):   
                    stack.pop()
                    stack.pop()
            
        if len(stack) >= 1:
            return False
        
        return True