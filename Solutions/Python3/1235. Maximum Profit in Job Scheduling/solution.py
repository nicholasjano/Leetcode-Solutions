class Solution:
    def binarySearch_left(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left


    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        n = len(jobs)

        dp = [0] * n
        start_times = [start_time for start_time, _, _ in jobs]

        for i in range(n - 1, -1, -1):
            start, end, profit = jobs[i]
            
            next_index = self.binarySearch_left(start_times, end)

            if next_index < n:
                profit += dp[next_index]

            dp[i] = max(profit, dp[i + 1] if i + 1 < n else 0)

        return dp[0]
