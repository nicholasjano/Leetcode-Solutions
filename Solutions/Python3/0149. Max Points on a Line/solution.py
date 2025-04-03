class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n
        
        max_points = 2
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]

                dy = y2 - y1
                dx = x2 - x1

                if dx == 0:
                    slope = ('inf', 0)
                elif dy == 0:
                    slope = (0, 0)
                else:
                    g = gcd(dy, dx)

                    dy //= g
                    dx //= g

                    if dx < 0:
                        dx *= -1
                        dy *= -1

                    slope = (dy, dx)
                
                slopes[slope] += 1

                max_points = max(max_points, slopes[slope] + 1)
        
        return max_points
