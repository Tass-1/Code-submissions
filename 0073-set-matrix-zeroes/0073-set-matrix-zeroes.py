class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for i in range(len(matrix)):
            curr = matrix[i]
            for j in range(len(curr)):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for r in row:
            for p in range(len(matrix[r])):
                matrix[r][p] = 0
        for c in col:
            for h in range(len(matrix)):
                matrix[h][c] = 0