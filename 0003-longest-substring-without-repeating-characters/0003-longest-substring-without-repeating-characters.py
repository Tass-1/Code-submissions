class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        k = set()
        minlen = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            while s[i] in k:
                k.remove(s[left])
                left += 1
                if s[i] not in k:
                    k.add(s[i])
                    break
            else:
                if (i-left+1)>minlen:
                    minlen = i-left+1
                k.add(s[i])
        print(k)
        return minlen