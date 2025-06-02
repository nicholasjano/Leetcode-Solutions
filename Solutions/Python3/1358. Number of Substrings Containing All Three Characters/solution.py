class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        occurences = defaultdict(int)
        substrings = 0
        left = 0
        for right in range(n):
            char_right = s[right]
            occurences[char_right] += 1
            while len(occurences) == 3:
                substrings += (n - right)
                char_left = s[left]
                occurences[char_left] -= 1
                if occurences[char_left] == 0:
                    del occurences[char_left]
                left += 1
        return substrings
