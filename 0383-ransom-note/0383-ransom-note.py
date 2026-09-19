class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ra = []
        for i in range(len(ransomNote)):
            ra.append(ransomNote[i])
        j = 0

        while j < len(magazine):
            if magazine[j] in ra:
                ra.remove(magazine[j])
            j += 1
        if len(ra) == 0:
            return True
        return False