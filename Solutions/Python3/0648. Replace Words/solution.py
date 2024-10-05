class Node:
    def __init__(self, data, end = False):
        self.data = data
        self.end = end
        self.next = {}

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        head = Node("")

        current_node = head

        for word in dictionary:
            word_length = len(word)
            for i, char in enumerate(word):
                if not current_node.next.get(char):
                    if i == word_length - 1:
                        current_node.next[char] = Node(char, True)
                    else:
                        current_node.next[char] = Node(char)
                current_node = current_node.next[char]
                if current_node.end:
                    break
                elif i == word_length - 1:
                    current_node.end = True
                    current_node.next = {}
            current_node = head

        sentence = sentence.split(" ")

        for i, word in enumerate(sentence):
            for j, char in enumerate(word):
                if current_node.next.get(char):
                    current_node = current_node.next[char]
                    if current_node.end:
                        sentence[i] = word[:j+1]
                else:
                    break
            current_node = head

        return " ".join(sentence)