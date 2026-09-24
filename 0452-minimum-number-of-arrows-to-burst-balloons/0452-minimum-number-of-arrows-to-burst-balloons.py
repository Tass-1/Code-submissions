from operator import itemgetter
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = itemgetter(1))
        count = 1
        k = points[0][1]
        for start , end in points:
            if start > k:
                count = count + 1
                k = end
        return count
        