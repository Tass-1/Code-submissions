class Solution:
    def romanToInt(self, s: str) -> int:
        di = {"I": 1 , "V": 5 , "X": 10, "L" : 50, "C": 100, "D": 500, "M": 1000}
        

        prev = di[s[0]]
        total = prev
        for i in range(1,len(s)):
            curr = di[s[i]]
            print(curr)
            if curr > prev:
                total -= prev
                total += curr - prev
                prev = curr
            else:
                total += curr
                prev = curr
            print(total)
        return total 
