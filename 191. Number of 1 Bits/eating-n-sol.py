class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0;
        mask = 1
        '''
        for each bit, get its number and check if it's 1 
        using & operator and mask
        
        '''
        while (n!=0):
            if (mask & n == 1): cnt +=1
            n = n >> 1
            
            
        return cnt;
    
