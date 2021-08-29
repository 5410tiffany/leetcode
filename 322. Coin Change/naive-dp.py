class Solution:
    def checkeach(self, end):
        for i in range(end):
            self.dp[end] = min(self.dp[end-i] + self.dp[i], self.dp[end])
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
        # coins = [1]
        # amount = 0
        self.dp = [inf] * (amount + 1)
        
        # init coins list as 1, dp[0] = 0
        self.dp[0] = 0
        for c in coins:
            if c > amount: pass
            elif c == amount: return 1
            else: self.dp[c] = 1
        # print(self.dp)
        
        # build dp sheet
        for i in range(1, amount + 1):
            self.checkeach(i)
        # print(self.dp)
        
        return -1 if (self.dp[amount] == inf) else self.dp[amount]
        
