class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        s1_swap_char = None
        s2_swap_char = None
        swap_found = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if swap_found:
                    return False
                
                if s1_swap_char:
                    if s1[i] == s2_swap_char and s2[i] == s1_swap_char:
                        swap_found = True
                    else:
                        return False
                else:
                    s1_swap_char = s1[i]
                    s2_swap_char = s2[i]
        
        return swap_found
        