class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        curr_sum_down = 0
        submatricies = 0
        for i in range(len(grid[0])): # cols
            if i > 0:
                grid[0][i] += grid[0][i-1]
            
            if grid[0][i] <= k:
                submatricies += 1
                curr_sum_down = grid[0][i]
                for j in range(1, len(grid)): #rows
                    if i > 0:
                        grid[j][i] += grid[j][i-1]
                    curr_sum_down += grid[j][i]
                    if curr_sum_down <= k:
                        submatricies += 1
                    else:
                        break
            else:
                break

        return submatricies