import math
class Solution:
    def maxArea(self, height: List[int]) :
        '''
        (height, idx) 
        想法:
        1. 算area只考慮height比自己大的 則area = heighti * abs(idxi - idxj)
        2. abs(idxi - idxj) 最大值必出現在idxj = minidx or maxidx 的地方
        
        time: O(n)
        greedy
        '''
        ls = []
        
        # buid (height, idx) 2D list
        for i in range(len(height)):
            ls.append([height[i], i])
        
        # sort according to height
        print(ls)
        ls.sort()
        print(ls)
        
        maxidx = ls[len(height)-1][1]
        minidx = ls[len(height)-1][1]
        maxarea = 0
        
        # iterate 
        for i in range(len(height)-2, -1, -1):
            
            curidx = ls[i][1]
            curheight = ls[i][0]
            print(f'{maxarea}: H-{ls[i][0]}, L-({maxidx}, {minidx}, {curidx}, {max(abs(maxidx-curidx), abs(minidx-curidx))})')
            
            # update area
            maxarea = max(maxarea, curheight * abs(maxidx-curidx), curheight * abs(minidx-curidx))
            # update idx
            maxidx = max(maxidx, ls[i][1])
            minidx = min(minidx, ls[i][1])
            
        

        print(maxarea)
        return maxarea
