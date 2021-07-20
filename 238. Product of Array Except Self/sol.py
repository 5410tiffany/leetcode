class Solution:
    def productExceptSelf(self, nums):
        '''
        no division: 得到答案只能用乘的-> ans_i = 左subprod * 右subprod
        '''

        lprod = []
        rprod = []
        ans = [-1] * len(nums) 
        
        lcur =  1
        rcur = 1
        
        # calculate accumulated product from left(lprod) and right(rprod)
        for i in range(len(nums)):
            lcur *= nums[i]
            rcur *= nums[len(nums)-1-i]
            lprod.append(lcur)
            rprod.append(rcur)
        
        rprod.reverse()
        
        # print(f'l: {lprod}')
        # print(f'r: {rprod}')
        # print(f'ans: {ans}')
        
        # calculate ans
        ans[0] = rprod[1]
        ans[len(nums)-1] = lprod[len(nums)-2] 
        for i in range(1, len(nums)-1):
            ans[i] = lprod[i-1] * rprod[i+1]
            
        return  ans                                                                                                              
