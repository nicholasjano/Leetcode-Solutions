class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            ASCII_difference = ord(s[i]) - ord(s[i+1])
            score += abs(ASCII_difference)
        return score