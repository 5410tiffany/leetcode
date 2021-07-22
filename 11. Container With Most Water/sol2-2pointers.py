
class Solution:
    def maxArea(self, height: List[int]) :
        '''
        (height, idx) 
        '''
        maxarea = 0
        l = 0
        r = len(height) - 1
        while (l < r):
            
            # update area 
            curarea = abs(r-l) * min(height[l], height[r])
            maxarea = max(maxarea, curarea)
            
            if (height[l] > height[r]):
                r -= 1
            else:
                l +=1
        return maxarea
