class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        alternations = 0
        current_length = 1
        prev_color = colors[0]
        for i in range(1, n + k - 1):
            index = i % len(colors)
            color = colors[index]
            if color != prev_color:
                current_length += 1
            else:
                current_length = 1
            
            prev_color = color
            
            if current_length >= k:
                alternations += 1
        
        return alternations
