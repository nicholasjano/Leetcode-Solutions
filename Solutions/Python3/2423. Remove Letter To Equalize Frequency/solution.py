class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = [0] * 26
        for char in word:
            freq[ord(char) - 97] += 1
        
        freq1 = freq2 = -1
        count1 = count2 = 0
        highest_num = 0
        amount_of_chars = 0
        for num in freq:
            if num > 0:
                if freq1 == -1:
                    freq1 = num
                elif num != freq1 and freq2 == -1:
                    freq2 = num
            
                if num == freq1:
                    count1 += 1
                elif num == freq2:
                    count2 += 1
                elif freq1 != -1 and freq2 != -1:
                    return False
                
                if count1 > 1 and count2 > 1:
                    return False
                
                highest_num = max(num, highest_num)

                if abs(highest_num - num) > 2 and num != 1:
                    return False

                amount_of_chars += 1

        if amount_of_chars == 1:
            return True
        elif amount_of_chars == 2 and (freq1 == 1 or freq2 == 1):
            return True
        elif amount_of_chars % 2 == 1 and freq1 != -1 and freq2 != -1:
            if highest_num > 2 and freq1 > 1 and freq2 > 1:
                if ((freq1 > freq2 and count1 > count2) or (freq2 > freq1 and count2 > count1)):
                    return False
        
        if freq2 == -1 and highest_num > 1:
            return False
        elif (freq1 != -1 and abs(highest_num - freq1) >= 2 and (freq1 > 1 or count1 > count2)) or (freq2 != -1 and abs(highest_num - freq2) >= 2 and (freq2 > 1 or count2 > count1)):
            return False
        
        return True