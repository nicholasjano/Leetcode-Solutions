class Solution:
    def isNumber(self, s: str) -> bool:
        return re.search("^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$", s)