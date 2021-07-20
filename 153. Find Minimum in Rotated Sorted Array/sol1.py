import bisect
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        binary search: find idx of 裂縫 
        裂縫 = 7 in [4567 [0]12]
        let: 
        4567 = large region
        012 = small region
        '''
        l = 0
        r = len(nums) - 1
        
        while (r>l):
            mid = math.floor( l + (r - l) / 2)
            
            # reached target
            # if nums[mid] <= nums[mid-1] and nums[mid] <= nums[mid+1]: 
            #     return nums[mid]
            
            # mid in left region
            if nums[mid] > nums[r]:
                l = mid + 1
            
            # mid in right region
            elif nums[mid] < nums[r]:
                r = mid
        
        return nums[l]
