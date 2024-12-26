class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        white = len(s) - 1
        ball_looking = 1
        swaps = 0

        while black <= white:
            if ball_looking == 1:
                ball = s[black]
                if ball == "1":
                    ball_looking = 0
                else:
                    black += 1
            else:
                ball = s[white]
                if ball == "0":
                    ball_looking = 1
                    swaps += white - black
                    black += 1
                white -= 1
        
        return swaps