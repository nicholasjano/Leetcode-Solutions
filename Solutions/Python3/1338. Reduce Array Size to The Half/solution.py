class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        target = len(arr) // 2
        set_size = 0

        num_count = Counter(arr)
        max_heap = []
        for key in num_count.keys():
            occurences = num_count[key]
            max_heap.append(-occurences)
        heapify(max_heap)

        while target > 0:
            largest = -max_heap[0]
            target -= largest
            heappop(max_heap)
            set_size += 1
        
        return set_size