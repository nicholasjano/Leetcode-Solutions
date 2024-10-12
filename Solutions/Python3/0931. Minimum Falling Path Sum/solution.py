class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for row in range(n-2, -1, -1):
            for col in range(n):
                val = matrix[row][col]

                path_digonal_left = inf
                if col - 1 >= 0:
                    path_digonal_left = val + matrix[row + 1][col - 1]
                
                path_digonal_right = inf
                if col + 1 < n:
                    path_digonal_right = val + matrix[row + 1][col + 1]

                path_down = val + matrix[row + 1][col]

                matrix[row][col] = min(path_digonal_left, path_digonal_right, path_down)
        
        return min(matrix[0])