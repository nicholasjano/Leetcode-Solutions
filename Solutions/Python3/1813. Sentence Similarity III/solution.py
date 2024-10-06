class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1_deque = deque(sentence1.split(" "))
        sentence2_deque = deque(sentence2.split(" "))

        while sentence1_deque and sentence2_deque and sentence1_deque[0] == sentence2_deque[0]:
            sentence1_deque.popleft()
            sentence2_deque.popleft()
        
        while sentence1_deque and sentence2_deque and sentence1_deque[-1] == sentence2_deque[-1]:
            sentence1_deque.pop()
            sentence2_deque.pop()
        
        return not sentence1_deque or not sentence2_deque