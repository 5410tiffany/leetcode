class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1. dp[i] = max sum of [0,i] for taking i
        2. dp[i] = max(dp[i-2], dp[i-3])  + nums[i]
        3. bc: dp[0] = nums[0] dp[1] = nums[1]
        '''

        
        dp = [None] * (len(nums) + 3)
        
        dp[0] = dp[1] = dp[2] = 0
        
        for i in range(3,len(nums) + 3):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i-3]
            
        return max(dp)
