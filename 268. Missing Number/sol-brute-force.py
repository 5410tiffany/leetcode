class Solution:
    def missingNumber(self, nums: List[int]):
        n = len(nums)
        for i in range(n+1):
            if i in nums: pass
            else: return i
        
