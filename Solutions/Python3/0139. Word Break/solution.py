class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)

        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n - 1, -1, -1):
            for word in words:
                w = len(word)
                if (i + w <= n) and (s[i:i + w] == word) and (dp[i + w]):
                    dp[i] = True
                    break

        return dp[0]