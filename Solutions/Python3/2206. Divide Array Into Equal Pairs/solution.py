class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                visited.remove(num)
            else:
                visited.add(num)
        return len(visited) == 0