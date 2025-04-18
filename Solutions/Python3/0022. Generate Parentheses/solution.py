class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(string, open_count=0, close_count=0):
            if len(string) == 2 * n:
                result.append("".join(string))
                return
            if open_count < n:
                string.append("(")
                backtracking(string, open_count + 1, close_count)
                string.pop()
            if close_count < open_count:
                string.append(")")
                backtracking(string, open_count, close_count + 1)
                string.pop()

        backtracking([])
        return result