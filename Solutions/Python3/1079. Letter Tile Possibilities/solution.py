class Solution:
    def getSequences(self, letter_counter: dict) -> int:
        total = 0
        for i in range(26):
            letter = chr(65 + i)
            if letter_counter[letter] == 0:
                continue

            letter_counter[letter] -= 1
            total += 1 + self.getSequences(letter_counter)
            letter_counter[letter] += 1
        return total
    
    def numTilePossibilities(self, tiles: str) -> int:
        letter_counter = Counter(tiles)
        return self.getSequences(letter_counter)