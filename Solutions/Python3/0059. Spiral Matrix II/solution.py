class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = []

        for _ in range(n):
            result.append([])
            for _ in range(n):
                result[-1].append(0)
        
        curr_direction = 0 # 0 right, 1 left, 2 down, 3 up
        curr = [0, 0]
        up_down_counter = 0
        left_right_counter = 0
        for i in range(1, n*n + 1):
            result[curr[0]][curr[1]] = i
            if curr_direction == 0:
                if (curr[1] + 1) == (n - left_right_counter):
                    curr_direction = 2
                    curr[0] += 1
                else:
                    curr[1] += 1
            elif curr_direction == 1:
                if curr[1] == (0 + left_right_counter):
                    curr_direction = 3
                    curr[0] -= 1
                    left_right_counter += 1
                else:
                    curr[1] -= 1
            elif curr_direction == 2:
                if (curr[0] + 1) == (n - up_down_counter):
                    curr_direction = 1
                    curr[1] -= 1
                    up_down_counter += 1
                else:
                    curr[0] += 1
            elif curr_direction == 3:
                if curr[0] == (0 + up_down_counter):
                    curr_direction = 0
                    curr[1] += 1
                else:
                    curr[0] -= 1
        return result
