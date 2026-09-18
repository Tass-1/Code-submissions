import copy
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = copy.deepcopy(matrix)
        i = len(matrix)-1
        j = 0
        idx = 0
        while i >= 0:
            t = []
            while j < len(matrix):
                if len(t) == len(matrix):
                    j += 1
                    i = len(matrix) - 1
                    print(matrix)
                    
                    matrix[idx] = t
                    t = []
                    idx += 1
                else:
                    t.append(temp[i][j])
                    i -= 1
            i-=1