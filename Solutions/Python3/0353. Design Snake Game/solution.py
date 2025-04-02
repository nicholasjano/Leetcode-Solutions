class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.snake = deque([(0, 0)])
        self.snake_positions = set([(0, 0)])
        self.score = 0
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        row, col = self.snake[-1]
        row += self.movement[direction][0]
        col += self.movement[direction][1]

        if (
            row < 0 or row >= self.height or
            col < 0 or col >= self.width
        ):
            return -1
        
        remove_tail = True
        if self.score < len(self.food):
            food_row, food_col = self.food[self.score]
            if row == food_row and col == food_col:
                self.score += 1
                remove_tail = False
        
        if remove_tail:
            old_row, old_col = self.snake.popleft()
            self.snake_positions.remove((old_row, old_col))
        
        if (row, col) in self.snake_positions:
            return -1
        
        self.snake.append((row, col))
        self.snake_positions.add((row, col))

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)