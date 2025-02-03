class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = {}
        result = []
        for num in nums:
            if visited.get(num):
                result.append(num)
                if len(result) == 2:
                    return result
            else:
                visited[num] = True
        