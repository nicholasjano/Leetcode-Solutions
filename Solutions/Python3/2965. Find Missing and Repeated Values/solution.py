class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}

        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        a = None
        b = None
        for num in range(1, n * n + 1):
            if num not in freq:
                b = num
            elif freq[num] == 2:
                a = num

        return [a, b]