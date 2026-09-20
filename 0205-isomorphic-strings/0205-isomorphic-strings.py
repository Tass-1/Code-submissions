class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = {}
        for i in range(len(s)):
            if s[i] not in s1:
                if t[i] in s1.values():
                    return False
                s1[s[i]] = t[i]
            else:
                if s1[s[i]] != t[i]:
                    return False
                

            
            
        print(s1)
        
       
        return True