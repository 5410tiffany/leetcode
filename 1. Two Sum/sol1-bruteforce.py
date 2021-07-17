class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        ans = []
        
        for i in range(n):
            for j in range(i+1, n):
                # print(f'{i}, {j}')
                if nums[i] + nums[j] == target: 
                    ans.append(i)
                    ans.append(j)
                    return ans
    
