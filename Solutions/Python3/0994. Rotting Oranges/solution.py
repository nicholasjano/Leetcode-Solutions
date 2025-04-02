class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque()
        fresh = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    queue.append((row, column, 0))
                elif grid[row][column] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        result = 0
        while queue:
            row, column, minutes = queue.popleft()
            result = max(result, minutes)

            for row_movement, column_movement in directions:
                new_row = row + row_movement
                new_column = column + column_movement

                if (
                    0 <= new_row < rows and
                    0 <= new_column < columns and
                    grid[new_row][new_column] == 1):

                    queue.append((new_row, new_column, minutes + 1))
                    grid[new_row][new_column] = 0
                    fresh -= 1
        
        if fresh > 0:
            return -1
        return result
