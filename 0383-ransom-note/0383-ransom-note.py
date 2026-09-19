class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ra = {}
        for i in range(len(magazine)):
            ra[magazine[i]] = ra.get(magazine[i] , 0) + 1
        j = 0
        while j < len(ransomNote):
            if ransomNote[j] not in ra or (ra[ransomNote[j]] == 0):
                return False
            ra[ransomNote[j]] -= 1
            j += 1
        return True