class Solution:
    def twosum(self, idx, nums, pairls):
        for i,j in pairls:
            curset = [nums[idx], nums[j], nums[i]]
            if idx < j and curset not in self.ans: 
                # print(f'--{i} , {j}, {curset}, {pairls}')
                self.ans.append(curset)
        return 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        數字相同idx不同也算distinct
        idx不同set組成相同不可重複計算
        1. 決定pair sum set: {pairsum: i, j}
        2. check if need_i in pair sum set && minidx > i  
        TLE
        '''
        nums.sort()
        self.ans = []
        pairset = defaultdict(list)
        
        
                
        # determine pair sum set
        for i in range(len(nums)-1, -1, -1):
            for j in range(i-1, -1, -1):
                psum = nums[i] + nums[j]
                # print(f'{i}, {j}, {psum}')
                pairset[psum].append((i,j)) # j smaller
                
        # print(pairset)
        
        # check if need_i in pairset
        for i in range(len(nums)):
            if -nums[i] in pairset: 
                self.twosum(i, nums, pairset[-nums[i]]) 
                
        return self.ans
            
        
        
        
        return
