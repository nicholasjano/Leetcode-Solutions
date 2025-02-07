class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = m - 1
        col = 0
        negatives = 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                negatives += (n - col)
                row -= 1
            else:
                col += 1
        
        
        return negatives
