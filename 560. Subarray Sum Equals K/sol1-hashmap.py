class Solution:
    def subarraySum(self, nums, k):
        '''
        hashmap {sum_i: no. of occurrences of sum_i}
        B.C: if sum_i - k = 0, cnt += 1 -> add {0,1} to hashmap
        '''
        sumtili = 0
        cnt = 0
        hashmap = {0: 1}
        
        for i in range(len(nums)):
            sumtili += nums[i]
            need = sumtili - k
            
            if need in hashmap:
                cnt += hashmap[need]
        
            hashmap[sumtili] = (hashmap[sumtili]+1) if sumtili in hashmap else 1

            
            # print(f'{nums}: {sumtili}, {need}')
            
        
        print(hashmap)
        
        return cnt
        
