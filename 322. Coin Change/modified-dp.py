class Solution:
    def checkeach(self, end):
        for c in self.coins:
            if end - c >= 0:
                self.dp[end] = min(self.dp[end-c] + 1, self.dp[end])
        return
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        1. dp(i) = 湊到i的最低硬幣數
        2. dp(i) = min(dp(i-k) + dp(i+k)) for k in range(i)
        3. b.c. 
            dp(c for c in coins) = 1 
            dp(0) = 0
            ** coin > amount的情況
        '''
        # debug
        # coins = [3]
        # amount = 4
        self.coins = coins
        self.dp = [inf] * (amount + 1)
        
        # init coins list as 1, dp[0] = 0
        self.dp[0] = 0

        # build dp ls
        for i in range(1, amount + 1):
            self.checkeach(i)
        print(self.dp)
        
        return -1 if (self.dp[amount] == inf) else self.dp[amount]
        
