class Solution:
    def checkSubarraySum(self, nums, k):
        '''
        reference: No.560
        O(n^2): TLE
        '''
        n = len(nums)
        numdict = {0: 1}
        
        
        for start in range(n):
            cursum = nums[start]
            
            for end in range(start+1, n):
                # print(f'{start}, {end}')
                cursum += nums[end]
                
                if cursum % k == 0:
                    return True
        
        # print(numdict)
        return False
