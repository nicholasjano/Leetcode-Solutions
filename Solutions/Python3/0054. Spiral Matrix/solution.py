class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        direction = 0 # 0 = right, 1 = down, 2 = left, 3 = up

        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4

        return result
