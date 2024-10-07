class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_len = 0
        left = 0
        visited = {}

        for right, char in enumerate(s):
            if visited.get(char) != None and visited[char] >= left:
                left = visited[char] + 1
            
            longest_substring_len = max(longest_substring_len, right - left + 1)
            visited[char] = right

        return longest_substring_len