class Solution:
    def maxProduct(self, nums: List[int]):
        '''
        maximum prod subarr.
        想法: not only最大；最小的資訊也要儲存
        dp[i][0] = mintili
        dp[i][1] = maxtili
        
        b.c. max(maxtili) 發生在init maxtili = 1的時候
        
        Space: O(n)
        '''
        maxtili = [nums[0]]
        mintili = [nums[0]]
        
        
        for i in range(1, len(nums)):
            curmax = max(maxtili[-1] * nums[i], mintili[-1] * nums[i], nums[i])
            curmin = min(maxtili[-1] * nums[i], mintili[-1] * nums[i], nums[i])
            
            maxtili.append(curmax)
            mintili.append(curmin)
            
        print(f'min: {mintili}, max: {maxtili}')
        return max(maxtili)
        
