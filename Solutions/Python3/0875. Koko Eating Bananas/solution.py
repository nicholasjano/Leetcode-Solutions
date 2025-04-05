class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        smallest_k = right
        while left <= right:
            k = (left + right) // 2

            h_spent = 0
            for pile in piles:
                h_spent += ceil(pile/k)
            
            if h_spent <= h:
                smallest_k = k
                right = k - 1
            elif h_spent > h:
                left = k + 1
        
        return smallest_k
