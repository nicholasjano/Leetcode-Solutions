class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        constants = ("a", "e", "i", "o", "u")
        words = sentence.split()
        for i, word in enumerate(words):
            new_word = ""
            if word[0].lower() in constants:
                new_word = word
            else:
                new_word = word[1:]
                new_word += word[0]
            
            new_word += "ma"
            new_word += "a" * (i + 1)
            words[i] = new_word
        
        return " ".join(words)