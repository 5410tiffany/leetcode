class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1. 狀態dp(i) = steps to ith stair, total n-1 stairs
        2. 轉移 dp(i) = dp(i-1) + dp(i-2)
        3. b.c. dp(0) = 1 dp(1) = 2
        '''
        prev1 = 1 
        prev2 = 2
        
        if n == 1: return prev1
        elif n == 2: return prev2 
        
        for i in range(2, n):
            cur_i = prev1 + prev2
            prev1 = prev2
            prev2 = cur_i
            
        return cur_i
