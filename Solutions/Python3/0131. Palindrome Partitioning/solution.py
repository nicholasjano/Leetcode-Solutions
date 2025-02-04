class Solution:
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr_partition = []
        
        def dfs(i):
            if i >= len(s):
                result.append(curr_partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    curr_partition.append(s[i:j+1])
                    dfs(j+1)
                    curr_partition.pop()
        
        dfs(0)
        return result
