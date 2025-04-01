class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        char_occurences = {}
        max_value = -1
        max_key = None
        for char in s:
            if char in char_occurences:
                char_occurences[char] += 1
                if char_occurences[char] > max_value:
                    max_key = char
                    max_value = char_occurences[char]
            else:
                char_occurences[char] = 1
                if char_occurences[char] > max_value:
                    max_key = char
                    max_value = char_occurences[char]
        
        result = [""] * len(s)

        if max_value > (len(s) + 1) // 2:
            return ""

        index = 0
        while max_value != 0:
            result[index] = max_key
            index += 2
            max_value -= 1
        
        del char_occurences[max_key]

        for char, count in char_occurences.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                result[index] = char
                index += 2
                count -= 1
        
        return "".join(result)