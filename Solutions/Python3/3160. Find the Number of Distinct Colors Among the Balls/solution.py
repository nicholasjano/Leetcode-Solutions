class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        visited_colours = {}
        visited_balls = {}
        count = 0
        for ball, colour in queries:
            if colour not in visited_colours or visited_colours[colour] == 0:
                if ball in visited_balls:
                    old_colour = visited_balls[ball]
                    visited_colours[old_colour] -= 1
                    if visited_colours[old_colour] > 0:
                        count += 1
                else:
                    count += 1
                visited_colours[colour] = 1
            elif not (ball in visited_balls and visited_balls[ball] == colour):
                visited_colours[colour] += 1
                if ball in visited_balls:
                    old_colour = visited_balls[ball]
                    visited_colours[old_colour] -= 1
                    if visited_colours[old_colour] == 0:
                        count -= 1
            
            visited_balls[ball] = colour
            result.append(count)

        return result
