class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        group_rights = []
        for left, right in intervals:
            if group_rights and left > group_rights[0]:
                heapreplace(group_rights, right)
            else:
                heappush(group_rights, right)
            
        return len(group_rights)
