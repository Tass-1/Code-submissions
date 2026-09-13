class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx = 0
        tidx = 0
        ct = 0
        while sidx < len(s) and tidx<len(t):
            tbh = s[sidx]
            curr = t[tidx%len(t)]
            if tbh == curr:
                sidx += 1
                tidx += 1
            else:
                tidx += 1
        if sidx == len(s):
            return True
        else:
            return False
