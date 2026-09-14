from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = {}
        for i in range(len(words)):
            curr = words[i]
            k[curr] = k.get(curr,0) + 1
        n = len(words[0])*len(words)
        left = 0
        right = n-1
        res = []
        while right < len(s):
            temp = {}
            j = s[left : right +1]
            for m in range(0,len(j),len(words[0])):
                hurr = j[m:m +len(words[0]) ]
                temp[hurr] = temp.get(hurr,0) + 1
            
            if temp == k:
                res.append(left)
            left += 1
            right += 1
        return res