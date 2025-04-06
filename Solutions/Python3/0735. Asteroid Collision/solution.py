class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) >= 2 and stack[-2] > 0 and stack[-1] < 0:
                left = stack.pop()
                right = stack.pop()

                if abs(left) > right:
                    stack.append(left)
                elif abs(left) < right:
                    stack.append(right)
        
        return stack