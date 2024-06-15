class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if k == 0:
            return w
        
        projects = list(zip(profits, capital))
        projects.sort(key=lambda pair: -pair[1])

        heap = []
        heapify(heap)

        while k > 0:
            while projects and projects[-1][1] <= w:
                heappush(heap, -projects[-1][0])
                projects.pop()
            
            if len(heap) > 0:
                w -= heappop(heap)
            else:
                return w
            
            k -= 1
        
        return w
