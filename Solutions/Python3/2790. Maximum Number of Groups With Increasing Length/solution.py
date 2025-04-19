class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        n = len(usageLimits)
        usageLimits = [min(limit, n) for limit in usageLimits]
        
        count = Counter(usageLimits)
        
        total_available = 0
        groups_formed = 0

        for limit in range(1, n + 1):
            for _ in range(count[limit]):
                total_available += limit
                if total_available >= groups_formed + 1:
                    total_available -= (groups_formed + 1)
                    groups_formed += 1
        
        return groups_formed
