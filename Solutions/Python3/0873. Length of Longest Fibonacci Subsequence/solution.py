class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        dp = [[0] * len(arr) for _ in range(len(arr))]
        max_len = 0

        for curr in range(2, len(arr)):
            start = 0
            end = curr - 1

            while start < end:
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    dp[end][curr] = dp[start][end] + 1
                    max_len = max(dp[end][curr], max_len)
                    end -= 1
                    start += 1

        if max_len:
            return max_len + 2
        return 0