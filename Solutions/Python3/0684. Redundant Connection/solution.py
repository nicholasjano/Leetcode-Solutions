class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [1] * n

        def union(node1, node2):
            node1_group = find(node1)
            node2_group = find(node2)

            if node1_group == node2_group:
                return False
            
            if rank[node1_group] > rank[node2_group]:
                parent[node2_group] = node1_group
            elif rank[node1_group] < rank[node2_group]:
                parent[node1_group] = node2_group
            else:
                parent[node1_group] = node2_group
                rank[node2_group] += 1
            
            return True
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        for edge in edges:
            node1, node2 = edge
            node1 -= 1
            node2 -= 1
            canUnion = union(node1, node2)
            if not canUnion:
                return edge
        