class MedianFinder:

    def __init__(self):
        self.lower_half = [] # max-heap for the lower end values
        self.upper_half = [] # min-heap for the higher end values
    
    def addNum(self, num: int) -> None:
        heappush(self.lower_half, -num)

        heappush(self.upper_half, -heappop(self.lower_half))

        if len(self.lower_half) < len(self.upper_half):
            heappush(self.lower_half, -heappop(self.upper_half))

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        else:
            return (-self.lower_half[0] + self.upper_half[0]) / 2