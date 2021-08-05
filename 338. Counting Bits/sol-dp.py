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
        
        P(x)=P(x/2)+(xmod2)
        '''
        n = 5
        ans = [0] * (n+1)
        
        for i in range(1, n+1):
            
            ans[i] = ans[i >> 1] + i % 2
            print(f'{i}, {i>>1}: {ans[i]}, {bin(ans[i])}, {ans[i >> 1]}, {bin(ans[i >> 1])} {i%2}')

        return ans
        
        
        
