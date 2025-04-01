class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_streak = 0
        streak = 1
        prev = s[0]
        valid_substrings = 0
        for i in range(1, len(s)):
            if s[i] == prev:
                streak += 1
            else:
                valid_substrings += min(prev_streak, streak)
                prev_streak = streak
                streak = 1
                prev = s[i]
        valid_substrings += min(prev_streak, streak)
        return valid_substrings
