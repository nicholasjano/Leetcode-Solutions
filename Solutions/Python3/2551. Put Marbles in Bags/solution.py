class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        min_heap = []
        max_heap = []
        for i in range(n - 1):
            num1 = weights[i]
            num2 = weights[i + 1]
            nums_sum = num1 + num2
            min_heap.append(nums_sum)
            max_heap.append(-nums_sum)
        
        heapify(min_heap)
        heapify(max_heap)

        min_result = 0
        max_result = 0
        for i in range(k - 1):
            min_result += heappop(min_heap)
            max_result -= heappop(max_heap)
        
        return max_result - min_result
