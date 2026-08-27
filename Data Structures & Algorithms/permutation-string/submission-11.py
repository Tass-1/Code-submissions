class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s1s = sorted(s1)
        while(right <= len(s2)):
            s22 = s2[left:right]
            print(s22)
            s22s = sorted(s22)
            if s22s == s1s:
                return True
            right += 1
            left += 1
        
        return False