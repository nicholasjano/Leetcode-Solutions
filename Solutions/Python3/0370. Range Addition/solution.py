class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        n = length
        difference = [0] * n
        for update in updates:
            start, end, inc = update
            difference[start] += inc
            if end < n - 1:
                difference[end + 1] -= inc
        
        for i in range(1, n):
            difference[i] += difference[i-1]
        return difference
