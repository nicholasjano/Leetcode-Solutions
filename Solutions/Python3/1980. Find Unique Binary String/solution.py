class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        for i in range(n):
            curr = nums[i][i]
            result.append("1" if curr == "0" else "0")
        
        return "".join(result)
