class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0;
        mask = 1;
    
        '''
        for each bit, get its number and check if it's 1 
        using & operator and mask
        
        '''
        for i in range(32): 
            if ((n & mask) != 0):
                cnt+=1;
            
            print(list(bin(mask)))
            mask = mask << 1 # left shift bit
        
        return cnt;
    
