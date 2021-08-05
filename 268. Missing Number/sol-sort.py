class Solution:
    def missingNumber(self, nums: List[int]):
        n = len(nums)
        nums.sort()
        nums.append(-1)
        print(nums)
        for i in range(n+1):
            if i != nums[i]: 
                return i
        
