class Solution:
    def smallestString(self, s: str) -> str:
        result = []
        first_char = s[0]
        curr_pos = 0

        if first_char == "a":
            for i, c in enumerate(s):
                if c == "a":
                    result.append(c)
                else:
                    curr_pos = i
                    break
            
            if len(result) == len(s):
                result[-1] = "z"
                return "".join(result)
        
        in_substring = True
        for j in range(curr_pos, len(s)):
            c = s[j]
            if c == "a":
                in_substring = False
            elif in_substring:
                c = chr(ord(c) - 1)
            result.append(c)
        
        return "".join(result)
