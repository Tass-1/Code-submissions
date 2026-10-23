from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = list(permutations(nums))
        k = []
        for p in res:
            k.append(list(p))
        return k