class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        seen = set()
        res = []
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        top = 0
        bottom = m-1
        right = n-1
        left = 0
        while left <= right and top <= bottom:
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top += 1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right,left-1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left += 1

        
        return res
