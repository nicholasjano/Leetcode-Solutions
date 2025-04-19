class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(s)
        pos = n - 1
        res = 0
        while pos >= 0:
            curr_char = s[pos]
            if pos > 0 and (mapping[s[pos - 1]] < mapping[curr_char]):
                res -= mapping[s[pos - 1]]
                pos -= 1
            
            res += mapping[curr_char]
            pos -=1
        
        return res
