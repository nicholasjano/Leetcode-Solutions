class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_started = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha() and word_started == -1:
                word_started = i
            elif not s[i].isalpha() and word_started != -1:
                return word_started - i
        
        return word_started + 1