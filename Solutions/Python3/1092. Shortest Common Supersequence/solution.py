class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for row in range(n + 1):
            dp[row][0] = row

        for col in range(m + 1):
            dp[0][col] = col

        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

        super_sequence = []
        row, col = n, m

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
            else:
                super_sequence.append(str2[col - 1])
                col -= 1

        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1
        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1

        return "".join(super_sequence[::-1])