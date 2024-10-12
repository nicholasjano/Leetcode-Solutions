class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest = 1
        current = 1
        for i in range(1, len(s)):
            if ord(s[i - 1]) - ord(s[i]) == -1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        return longest
