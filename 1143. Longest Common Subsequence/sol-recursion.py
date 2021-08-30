class Solution:
    def memo_solve(self, p1, p2): # 'a' is at idx p1 in text1
        
        # terminal pt if either subseq is empty
        if p1 == len(self.text1) or p2 == len(self.text2): return 0
        
        
        # no: 'a' not in optimal sol 
        optnop1 = self.memo_solve(p1 + 1, p2)
        
        # yes: 'a' in optimal sol
        p1intext2 = self.text2.find(self.text1[p1], p2) # find 'a' start from position p2
        optyesp1 = 0
        
        if p1intext2 != -1: # 'a' is in p2 subseq
            optyesp1 = self.memo_solve(p1 + 1, p1intext2 + 1) + 1
        
        return max(optnop1, optyesp1)
    def longestCommonSubsequence(self, text1: str, text2: str):
        '''
        break down into subproblem: a 是不是在optimal sol中
        1. no -> lcs(s1, s2) = lcs(s1-a, s2)
        2. yes-> lcs(s1, s2) = lcs(s1-a, s2-a) + 1
        '''
        #debug 
        # text1 ='aaaa'
        # text2 = 'aaaa'
        
        #speed up
        if text2 in text1 or text1 in text2: 
            return min(len(text1), len(text2))
        
        self.text1 = text1
        self.text2 = text2

        
        return self.memo_solve(0, 0)
        
        
        
        
