class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        def pathTraversal(row, column, moves_remaining):
            if not 0 <= row < m or not 0 <= column < n or grid[row][column] == -1:
                return 0
            
            if moves_remaining == 0 or grid[row][column] == 2:
                if moves_remaining == 0 and grid[row][column] == 2:
                    return 1
                return 0
            
            grid[row][column] = -1

            left = pathTraversal(row, column - 1, moves_remaining - 1)
            right = pathTraversal(row, column + 1, moves_remaining - 1)
            up = pathTraversal(row - 1, column, moves_remaining - 1)
            down = pathTraversal(row + 1, column, moves_remaining - 1)

            grid[row][column] = 0

            return left + right + up + down


        start_row = -1
        start_column = -1
        obstacles = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_row = i
                    start_column = j
                elif grid[i][j] == -1:
                    obstacles += 1
        
        return pathTraversal(start_row, start_column, m*n-obstacles-1)