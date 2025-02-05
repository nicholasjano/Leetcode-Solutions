class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        max_substring = s[0]
        # Odd Legthed
        current_length = 1
        for i in range(1, len(s) - 1):
            left = i-1
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length += 2
                if current_length > len(max_substring):
                    max_substring = s[left:right+1]

                left -= 1
                right += 1
            
            current_length = 1
        
        # Even Lengthed
        current_length = 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                left = i-1
                right = i+2
                
                current_length = 2
                if current_length > len(max_substring):
                    max_substring = s[i:i+2]
                
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    current_length += 2
                    if current_length > len(max_substring):
                        max_substring = s[left:right+1]

                    left -= 1
                    right += 1
                
                current_length = 1

        return max_substring
