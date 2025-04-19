class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial = image[sr][sc]
        
        if initial == color:
            return image
        
        m = len(image)
        n = len(image[0])

        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        queue = deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for r_dir, c_dir in directions:
                new_r = r + r_dir
                new_c = c + c_dir

                if (
                    0 <= new_r < m and
                    0 <= new_c < n and
                    image[new_r][new_c] == initial
                ):
                    queue.append((new_r, new_c))
        
        return image
