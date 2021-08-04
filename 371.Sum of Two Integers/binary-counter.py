class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        XOR manipulation
        '''
        x, y = abs(a), abs(b)
        
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)
        
        # abs(a) >= abs(b): 
        # a determines the sign
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            '''
            sum of two positive/negative integers x + y
            where x > y
            consider carry only
            XOR manipulation: a ^ b
            '''
            
            # TODO
            while y:
                ans = x ^ y
                carry = (x & y) << 1
                x, y = ans, carry 
                print(x, y)
            
        else:
            '''
            difference of two integers x - y
            where x > y
            consider borrow only
            '''

            # TODO
            pass
            while y:
                ans = x ^ y
                borrow = ((~x) & y) << 1
                x,y = ans, borrow
                
        
        return x * sign
