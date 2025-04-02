class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        max_count = -1
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            
            max_count = max(max_count, counter[num])
        
        buckets = [[] for _ in range(max_count)]
        for key, count in counter.items():
            buckets[count - 1].append(key)
        
        result = []
        for i in range(max_count - 1, -1, -1):
            bucket = buckets[i]
            for num in bucket:
                result.append(num)
                k -= 1
                if k == 0:
                    return result