class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        k = k[::-1]
        res = ""
        for i in range(len(k)):
            if i == 0:
                res += k[i]
            else:
                res += " " + k[i] 
        return res