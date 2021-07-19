class Solution:
  '''
  set / hash func.
  '''
    def containsDuplicate(self, nums):
        exist = set()
        for n in nums:
            if n in exist:
                return True
            exist.add(n)
                
            
        return False
        
