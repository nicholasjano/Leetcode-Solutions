class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        remaining = Counter({"a":a, "b":b, "c":c})
        s = ""
        while True:
            (most_common, _), (second_common, _) = remaining.most_common(2)

            if len(s) >= 2 and most_common == s[-1] == s[-2]:
                most_common = second_common
            
            if remaining[most_common] == 0:
                return s
            
            s += most_common
            remaining[most_common] -= 1