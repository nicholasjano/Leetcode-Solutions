class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0]
        for node in edges[1]:
            if node in first:
                return node