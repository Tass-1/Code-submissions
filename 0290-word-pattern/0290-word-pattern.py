class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k = s.split()
        if len(k) != len(pattern):
            return False
        s1 = {}
        for i in range(len(k)):
            if pattern[i] not in s1:
                if k[i] in s1.values():
                    return False
                s1[pattern[i]] = k[i]
            else:
                if s1[pattern[i]] != k[i]:
                    return False

        return True