class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        k = -1
        res = []
        if len(intervals) == 0:
            return []
        intervals.sort()
        print(intervals)
        for i in range(len(intervals)):

            curr = intervals[i]
            if curr[0] <= k and curr[1] >= k:
                res[-1][1] = curr[1]
                k = curr[1]
            elif curr[0] <= k >= curr[1]:
                continue
            else:
                k = curr[1]
                res.append(curr)
        return res