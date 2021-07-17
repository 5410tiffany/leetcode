class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        numdict = defaultdict(int)
        
        for i in range(n):
            if nums[i] in numdict:
                return [i, numdict[nums[i]]]
            
            need = target - nums[i]
            numdict[need] = i
            # print(numdict)
            
        
        

    
        
