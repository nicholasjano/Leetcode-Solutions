class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        
        forward_queue = deque([beginWord])
        backward_queue = deque([endWord])
        
        forward_visited = {beginWord: 1}
        backward_visited = {endWord: 1}
        
        while forward_queue and backward_queue:
            if len(forward_queue) <= len(backward_queue):
                found = self.bfs(forward_queue, forward_visited, backward_visited, wordSet)
                if found > 0:
                    return found
            else:
                found = self.bfs(backward_queue, backward_visited, forward_visited, wordSet)
                if found > 0:
                    return found
        
        return 0
    
    def bfs(self, queue, visited, other_visited, wordSet):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        level_size = len(queue)
        for _ in range(level_size):
            curr_word = queue.popleft()
            curr_dist = visited[curr_word]
            
            for i in range(len(curr_word)):
                prefix, suffix = curr_word[:i], curr_word[i+1:]
                for c in alphabet:
                    if c == curr_word[i]:
                        continue
                    
                    next_word = prefix + c + suffix
                    
                    if next_word in other_visited:
                        return curr_dist + other_visited[next_word]
                    
                    if next_word in wordSet and next_word not in visited:
                        visited[next_word] = curr_dist + 1
                        queue.append(next_word)
        
        return 0