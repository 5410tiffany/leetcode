class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0 
        r = len(height) - 1
        rmax = 0
        lmax = 0
        area = 0
        
        while (l < r):
            if height[l] > height[r]: 
                rmax = max(rmax, height[r])
                r -= 1
                area += max(rmax- height[r], 0)
                
            else:
                lmax = max(lmax, height[l])
                l += 1
                area += max(lmax- height[l], 0)
                
            
            # print(f'{l}, {r}, {lmax}, {rmax}')
        
        return area
