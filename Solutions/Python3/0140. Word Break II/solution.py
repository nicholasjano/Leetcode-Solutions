class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)
        memo = {}
        def backtracking(start=0):
            if start == n:
                return [""]
            
            if start in memo:
                return memo[start]

            result = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word not in words:
                    continue
                
                strings = backtracking(end)
                if not strings:
                    continue

                for substring in strings:
                    sentence = word
                    if substring:
                        sentence += f" {substring}"
                    result.append(sentence)
            
            memo[start] = result
            return result

        return backtracking()
