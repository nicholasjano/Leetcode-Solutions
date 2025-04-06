class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        min_sums = 0

        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] > arr[i]):
                popped_index = stack.pop()
                num = arr[popped_index]
                left = popped_index - stack[-1] if stack else popped_index + 1
                right = i - popped_index
                min_sums = (min_sums + num * left * right) % MOD
            stack.append(i)

        return min_sums