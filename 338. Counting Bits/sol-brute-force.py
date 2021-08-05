class Solution:
    def countBits(self, n: int):
        '''
        Input: n = 5
        Output: [0,1,1,2,1,2]
        Explanation:
        0 --> 0   # 0 1s
        1 --> 1   # 1 1s
        2 --> 10  # 1 1s
        3 --> 11  # 2 1s
        4 --> 100 # 1 1s
        5 --> 101 # 2 1s
        '''
        ls = []
        for i in range(n+1):
            cnt = bin(i).count('1')
            ls.append(cnt)
        
        return ls
        
