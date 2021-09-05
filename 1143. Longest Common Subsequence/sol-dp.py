class Solution:
    # def lcs(self,p1,p2):
    #     # terminal pt
    #     if len(self.text1[p1] == 0 or self.text2[p2] == 0): 
    #         return 0
    #     else return lcs()
        
    def longestCommonSubsequence(self, text1: str, text2: str):
        '''
        break down into subproblem: a 是不是在optimal sol中
        1. dp[i,j] = lcs[i,j]
        2. dp[i,j] = max(lcs[i+1,j], lcs[i,j+1])
        3. b.c.: lcs[m,n] = lcs[i,0] = lcs[0,j] 
        '''
        #debug 
        # text1 ='aaaa'
        # text2 = 'aaaa'
        
        #speed up
        if text2 in text1 or text1 in text2: 
            return min(len(text1), len(text2))
        
        col = len(text1)
        row = len(text2)
        
        # build dp
        dp = [ [0]*(col+1) for _ in range(row+1) ]
        dp[row-1][col-1] = 1 if text2[row-1] == text1[col-1] else 0
        
        # build b.c.
        # for i in range(col):
        #     dp[row-1][i] = dp[row-1][col-1]
        # for i in range(row):
        #     dp[i][col-1] = dp[row-1][col-1]
        
        # print(dp)
        
        for i in range(row-1, -1, -1): 
            for j in range(col-1, -1, -1):
                if text1[j] == text2[i]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        print(dp)
        return dp[0][0]
        
        
        
        
