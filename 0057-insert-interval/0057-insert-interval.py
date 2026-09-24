class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        prev = newInterval[0]
        nex = newInterval[1]
        k = -1
        intervals.append(newInterval)
        res = []
        intervals.sort()
        print(intervals)
        for i in range(len(intervals)):
            curr = intervals[i]
            print(res)
            if curr[0] <= k and curr[1] >= k:
                res[-1][1] = curr[1]
                k = curr[1]
            elif curr[0] <= k >= curr[1]:
                continue
            else:
                k = curr[1]
                res.append(curr)
        return res
        
        
        print(intervals)

