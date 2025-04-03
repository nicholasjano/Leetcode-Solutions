class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(row, col, position=0):
            if (
                not (0 <= row < m) or
                not (0 <= col < n) or
                board[row][col] != word[position]
            ):
                return False

            if position + 1 == len(word):
                return True
            
            original = board[row][col]
            board[row][col] = "#"
            
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if dfs(new_row, new_col, position + 1):
                    return True
                
            board[row][col] = original
            return False

        word_count = defaultdict(int)
        for c in word:
            word_count[c] += 1

        board_count = defaultdict(int)
        for i in range(m):
            for j in range(n):
                board_count[board[i][j]] += 1
        
        for char, occurences in word_count.items():
            if board_count[char] < occurences:
                return False
        
        if word_count[word[0]] > word_count[word[-1]]:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    return True

        return False
