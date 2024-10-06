class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        visited_chars = {}
        sum = 0
        for i in range(len(s)):
            if visited_chars.get(s[i]) is not None:
                sum += (i - visited_chars[s[i]])
            else:
                visited_chars[s[i]] = i
            if visited_chars.get(t[i]) is not None:
                sum += (i - visited_chars[t[i]])
            else:
                visited_chars[t[i]] = i
        return sum