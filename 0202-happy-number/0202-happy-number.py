class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        t = n
        su = 0
        count = 0
        while t != 1 and count < 20:
            count += 1
            digs = []
            su = 0
            while t > 0:
                d = t%10
                digs.append(d)
                t = t//10
            print(digs)
            for num in digs:
                su += num**2
            print(su)
            t = su
        
        if su != 1:
            return False
        return True
        
        
