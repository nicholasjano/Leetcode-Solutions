class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        k = len(nums)
        left_bound = inf
        right_bound = -inf
        index_positions = [0] * k

        for i in range(k):
            new_num = nums[i][index_positions[i]]
            left_bound = min(left_bound, new_num)
            right_bound = max(right_bound, new_num)
            heappush(heap, (new_num, i))
            index_positions[i] += 1
        
        smallest_range = [left_bound, right_bound]

        while True:
            _, i = heap[0]
            if index_positions[i] < len(nums[i]):
                new_num = nums[i][index_positions[i]]
                heapreplace(heap, (new_num, i))
                index_positions[i] += 1
                left_bound = heap[0][0]
                right_bound = max(right_bound, new_num)

                if right_bound - left_bound < smallest_range[1] - smallest_range[0]:
                    smallest_range = [left_bound, right_bound]
            else:
                return smallest_range
