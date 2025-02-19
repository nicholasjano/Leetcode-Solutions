class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ["a", "b", "c"]
        result = []
        curr_result = []

        def dfs(letter = 0):
            if letter == n:
               result.append("".join(curr_result))
               return
            
            for c in chars:
                if curr_result and c == curr_result[-1]:
                    continue
                

                curr_result.append(c)
                dfs(letter + 1)
                curr_result.pop()
        
        dfs()
        if len(result) < k:
            return ""
        return sorted(result)[k-1]