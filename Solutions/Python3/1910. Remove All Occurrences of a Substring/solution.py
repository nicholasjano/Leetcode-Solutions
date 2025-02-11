class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = []
        part_length = len(part)
        target_char = part[-1]
        for c in s:
            result.append(c)
            if len(result) >= part_length and c == target_char and "".join(result[-part_length:]) == part:
                del result[-part_length:]
        
        return "".join(result)