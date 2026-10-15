class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows , col = len(board), len(board[0])
        visited = set()
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=col or board[r][c] == "X" or (r,c) in visited:
                return
            board[r][c] = "M"
            visited.add((r,c))
            for dr , dc in [(1,0), (-1,0),(0,1),(0,-1)]:
                dfs(r+dr, c+dc)
            
            
        for i in range(rows):
            for j in range(col):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == rows-1 or j == col-1):
                    dfs(i,j)
                
        for k in range(rows):
            for m in range(col):
                if board[k][m] == "M":
                    board[k][m] = "O"
                elif board[k][m] == "O":
                    board[k][m] = "X"
        