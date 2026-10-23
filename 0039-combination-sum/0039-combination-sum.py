class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        m = target / min(candidates)
        def search(ip , path):
            if sum(path) > target:
                return
            if sum(path) == target:
                a = path.copy()
                res.append(a)
                return
            for i in range(ip, len(candidates)):
                path.append(candidates[i])
                search(i,path)
                path.pop()
        search(0,[])
        return res