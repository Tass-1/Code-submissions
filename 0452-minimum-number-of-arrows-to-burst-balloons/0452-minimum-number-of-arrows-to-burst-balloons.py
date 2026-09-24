class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x:x[1])
        print(points)
        count = 1
        k = points[0][1]
        for curr in points:
            if curr[0] > k:
                count += 1
                k = curr[1]
            k = min(curr[1],k)
        return count
        