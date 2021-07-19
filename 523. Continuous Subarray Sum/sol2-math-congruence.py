class Solution:
    def checkSubarraySum(self, nums, k):
        '''
        prefix(sum til index i) 同餘則兩prefix 相減為k的倍數
        '''
        

        
        prefix = nums[0]
        dup = set()
        dup.add(prefix % k)
        
        for i in range(1, len(nums)):

            prefix += nums[i]
            print(f'{i}: {prefix}, {nums[i]}, {prefix % k}, set: {dup}')
            
            
            # (同餘 or prefix整除) and (subarr不可只有自己)
            if (prefix % k in dup or prefix % k == 0) and nums[i] % k != 0:
                return True
            
            # b.c. [7,7,7,7] k = 7 解決上面排除掉的nums[i] % k != 0 特例
            if nums[i - 1] % k == 0 and nums[i] % k == 0: 
                return True
            

            dup.add(prefix % k)
            
            
        return False
