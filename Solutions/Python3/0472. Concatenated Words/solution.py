class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        answer = []
        words = set(words)
        for search_word in words:
            words.remove(search_word)
            
            m = len(search_word)
            dp = [False] * (m + 1)
            dp[-1] = True

            for i in range(m - 1, -1, -1):
                for j in range(m, i, -1):
                    if dp[j] and (search_word[i:j] in words):
                        dp[i] = True
            
            if dp[0]:
                answer.append(search_word)
            
            words.add(search_word)
        
        return answer
