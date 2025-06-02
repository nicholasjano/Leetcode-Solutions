class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = "aeiou"

        def atLeastK(k):
            vowel = defaultdict(int)
            non_vowel_count = 0
            substrings = 0

            left = 0
            for right in range(n):
                r_char = word[right]
                if r_char in vowels:
                    vowel[r_char] += 1
                else:
                    non_vowel_count += 1
                
                while len(vowel) == 5 and non_vowel_count >= k:
                    substrings += (n - right)
                    l_char = word[left]
                    if l_char in vowels:
                        vowel[l_char] -= 1
                    else:
                        non_vowel_count -= 1
                    
                    if vowel[l_char] == 0:
                        del vowel[l_char]

                    left += 1
            
            return substrings
        
        return atLeastK(k) - atLeastK(k + 1)