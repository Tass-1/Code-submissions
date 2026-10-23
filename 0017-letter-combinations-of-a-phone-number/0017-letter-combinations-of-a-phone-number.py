from itertools import permutations
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        nums = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        if not digits:
            return []
        res = []
        def search(id,pa):
            if id == len(digits):
                res.append("".join(pa))
                return
            
            num = digits[id]
            letters = nums[num]

            for l in letters:
                pa.append(l)
                search(id+1,pa)
                pa.pop()
        search(0,[])
        return res
