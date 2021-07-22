class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        permutation: 排列
        in place: 直接原地此處理資料(no extra data structure created)
        
        想法: 
        numa: first decreasing element
        numb: first element b where numb > numa and (numb-numa) minimized
        """
        
        numa = -inf
        idxa = -1
        idxb = -1
        
        # find numsa: first decreasing element 
        for i in range(len(nums)-1, -1, -1):
            if  nums[i] < numa:
                idxa = i
                numa = nums[i]
                break
                
            numa = nums[i]
    
        # ls is in increasing order -> reverse the whole ls 
        if idxa==-1: 
            print(f'{i}, {nums}, {nums[::-1]}')
            nums.reverse()
            return 

        # print('yoooo')
        # find numsb: number just larger than numsa
        for j in range(idxa+1, len(nums), 1):
            if nums[j] <= numa:
                numsb = nums[j-1]
                idxb = j-1
                break
            numb = nums[j]
        
        # subls is all greater than idxa -> swap with the smallest 
        if idxb==-1: 
            numsb = nums[len(nums)-1]
            idxb = len(nums)-1
        
        # swap
        nums[idxa], nums[idxb] = nums[idxb], nums[idxa]
        print(f'{idxa}, {idxb}, {nums}')
        
        # reverse interval
        nums[idxa+1:] = nums[idxa+1:][::-1] 
        print(nums)
        
        return

        


       
        
