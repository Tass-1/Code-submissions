class Solution:
    def convert(self, s: str, numRows: int) -> str:
        word = [[] for _ in range(numRows)]
        rev = False
        idx = 0
        i = 0
        if numRows == 1:
            return s
        while i < len(s):
            curr = s[i]
            
            if rev == False:
                word[idx].append(curr)
                i+=1
                if idx == numRows-1 and i != 0:
                    rev = not rev
                    idx -= 1
                else:
                    idx += 1
            elif rev == True:
                word[idx].append(curr)
                i+=1
                if idx == 0 and i != 0:
                    rev = not rev
                    idx += 1
                else:
                    idx -= 1
        
        k = ""
        for i in range(numRows):
            
            k += "".join(word[i])
        return k
            