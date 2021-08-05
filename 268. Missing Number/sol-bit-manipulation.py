class Solution:
    def missingNumber(self, nums: List[int]):
        '''
        自己 XOR 自己 = 0
        '''
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
