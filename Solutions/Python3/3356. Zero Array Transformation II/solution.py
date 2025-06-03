class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        k = len(queries)
        accumulated_reduction = 0
        queries_index = 0
        difference = [0] * (n + 1)
        
        for i in range(n):
            current_reduction = accumulated_reduction + difference[i]
            while current_reduction < nums[i] and queries_index < k:
                left, right, val = queries[queries_index]
                if right >= i:
                    difference[max(left, i)] += val
                    difference[right + 1] -= val
                    if left <= i:
                        current_reduction += val
                
                queries_index += 1
            
            if current_reduction < nums[i]:
                return -1
            
            accumulated_reduction += difference[i]
        
        return queries_index