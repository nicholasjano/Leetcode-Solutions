class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        max_len = 0
        current_cost = 0
        while right < len(s):
            new_index_difference = abs(ord(s[right]) - ord(t[right]))

            if new_index_difference > maxCost:
                right += 1
                left = right
                current_cost = 0
                continue
            
            while current_cost + new_index_difference > maxCost:
                tail_index_difference = abs(ord(s[left]) - ord(t[left]))
                current_cost -= tail_index_difference
                left += 1
            
            current_cost += new_index_difference
            
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len
