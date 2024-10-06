class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        visited = {}
        pairs = 0
        for num in nums:
            if visited.get(num - k):
                pairs += visited.get(num - k)
            if visited.get(num + k):
                pairs += visited.get(num + k)
            if not visited.get(num):
                visited[num] = 0
            visited[num] += 1
        return pairs
        