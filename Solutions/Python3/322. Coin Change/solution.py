class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                coin_complement = i - coin
                if coin_complement >= 0:
                    dp[i] = min(dp[i], 1 + dp[coin_complement])

        if dp[-1] == amount + 1:
            return -1
        
        return dp[-1]