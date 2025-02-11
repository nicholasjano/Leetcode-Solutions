class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        amt_to_remove = 0
        for c in reversed(s):
            if c.isnumeric():
                amt_to_remove += 1
            else:
                if amt_to_remove == 0:
                    result.append(c)
                else:
                    amt_to_remove -= 1
        
        return "".join(reversed(result))
