class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort(key = lambda x : len(x))
        s = strs[0]
        i = 1
        res = ""
        while i <= len(s):
            p = s[:i]
            t = True
            for st in strs:
                if p not in st[:i]:
                    t =False
            if t == True:
                res = p
            i+=1
        
        return res
        