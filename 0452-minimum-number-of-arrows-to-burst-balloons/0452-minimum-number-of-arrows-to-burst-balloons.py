class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x:x[1])
        count = 1
        k = points[0][1]
        for start , end in points:
            if start > k:
                count = count + 1
                k = end
        return count
        