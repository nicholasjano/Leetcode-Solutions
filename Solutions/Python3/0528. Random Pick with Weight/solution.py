class Solution:

    def __init__(self, w: List[int]):
        sum_w = sum(w)
        w[0] = w[0] / sum_w
        for i in range(1, len(w)):
            w[i] = (w[i] / sum_w) + w[i - 1]
        self.w = w

    def pickIndex(self) -> int:
        randon_number = random.random()
        low = 0
        high = len(self.w) - 1

        while low <= high:
            mid = (high + low) // 2
            probability = self.w[mid]
            if randon_number < probability:
                high = mid - 1
            elif randon_number > probability:
                low = mid + 1
            else:
                return mid
        
        return low

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()