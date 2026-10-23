from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # res = list(permutations(nums))
        # k = []
        # for p in res:
        #     k.append(list(p))
        # return k

        res = []
        def search(pa):
            print(pa)
            if len(pa) == len(nums):
                res.append(pa.copy())
                return
            
            for p in nums:
                if p in pa:
                    continue
                pa.append(p)
                search(pa)
                pa.pop()
        search([])
        return res
