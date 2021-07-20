import bisect
class Solution:
    def istarget(self, mid, nums) -> bool:
        
        midleft = nums[mid] if mid == 0 else nums[mid-1]
        midright = nums[mid] if mid == (len(nums) - 1) else nums[mid+1]
        if nums[mid-1] >= nums[mid] and nums[mid+1] >= nums[mid]: 
            return True
        return False
    
    def findMin(self, nums: List[int]) -> int:
        '''
        binary search: find idx of 裂縫 
        裂縫 = 7 in [4567 [0]12]
        let: 
        4567 = large region
        012 = small region
        b.c. determine target時要考慮mid是不是在0 or len(nums)-1的位置
        '''
        
        l = 0
        r = len(nums) - 1
        
        while (r>l):
            mid = math.floor( l + (r - l) / 2)
            
            # reached target
            if self.istarget(mid, nums): 
                return nums[mid]
            
            # mid in left region
            if nums[mid] > nums[r]:
                l = mid + 1
            
            # mid in right region
            elif nums[mid] < nums[r]:
                r = mid
        
        return nums[l]

        
