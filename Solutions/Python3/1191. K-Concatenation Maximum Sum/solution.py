class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = (10**9 + 7)
        max_subarray_sum = 0
        curr_subarray_sum = 0
        max_at_points = []

        for i in range(1, 4):
            for num in arr:
                curr_subarray_sum = max(0, curr_subarray_sum + num)
                max_subarray_sum = max(max_subarray_sum, curr_subarray_sum)
        
            if k == i:
                return max_subarray_sum % MOD

            max_at_points.append(max_subarray_sum)

            if i == 2 and max_at_points[0] == max_at_points[1]:
                return max_at_points[1] % MOD

        if max_at_points[1] == max_at_points[2]:
            return max_at_points[1] % MOD
        
        difference = max_at_points[2] - max_at_points[1]
        base = max_at_points[0] - difference

        base_mod = base % MOD
        k_mod = k % MOD
        difference_mod = difference % MOD
        term = (k_mod * difference_mod) % MOD
        result = (base_mod + term) % MOD

        return result
