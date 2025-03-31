class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    queue = deque([(row, column)])
                    grid[row][column] = "0"
                    while queue:
                        pos_row, pos_column = queue.popleft()

                        if pos_row > 0 and grid[pos_row - 1][pos_column] == "1":
                            queue.append((pos_row - 1, pos_column))
                            grid[pos_row - 1][pos_column] = "0"
                        if pos_column > 0 and grid[pos_row][pos_column - 1] == "1":
                            queue.append((pos_row, pos_column - 1))
                            grid[pos_row][pos_column - 1] = "0"
                        if pos_row + 1 < rows and grid[pos_row + 1][pos_column] == "1":
                            queue.append((pos_row + 1, pos_column))
                            grid[pos_row + 1][pos_column] = "0"
                        if pos_column + 1 < columns and grid[pos_row][pos_column + 1] == "1":
                            queue.append((pos_row, pos_column + 1))
                            grid[pos_row][pos_column + 1] = "0"
        
        return islands
