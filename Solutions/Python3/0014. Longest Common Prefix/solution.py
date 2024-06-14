class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        counter = 0
        while len(strs[0]) - 1 >= counter:
            current_char = strs[0][counter]
            for i in range(1, len(strs)):
                if len(strs[i]) - 1 < counter or strs[i][counter] != current_char:
                    return prefix
            prefix += current_char
            counter += 1
        return prefix