class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        n = len(digits)
        result = []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(s=[], index=0):
            if index == n:
                result.append("".join(s))
                return
            
            chars = mapping[digits[index]]
            for char in chars:
                s.append(char)
                dfs(s, index + 1)
                s.pop()
            return
        
        dfs()
        return result
