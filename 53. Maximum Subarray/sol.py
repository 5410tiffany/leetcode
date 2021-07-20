class Solution:
    def maxSubArray(self, nums):
        '''
        想法: sum of subarr(k,i) =  (0-i sum of subarr) - (0-k sum of subarr)
        b.c.
        1. 只有一個element的情況
        2. ans 是第一個
        
        Time: O(n)
        Space: O(1)
        '''
        if len(nums) == 1: return nums[0]
        
        mintili = 0
        cursum = 0
        ans = -inf
        
        for i in range(len(nums)):
            cursum += nums[i]
            ans = max(ans, cursum - mintili)
            mintili = min(cursum, mintili)
            
        print(f'{mintili}')
        return ans
        
