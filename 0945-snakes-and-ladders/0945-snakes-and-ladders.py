from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        
        def get_coordinates(square):
            row_from_bottom = (square - 1) // n
            r = (n - 1) - row_from_bottom
            c = (square - 1) % n
            if row_from_bottom % 2 != 0:
                c = (n - 1) - c
            return r, c
        
        queue = deque([(1, 0)])
        visited = set([1])
        
        while queue:
            curr, rolls = queue.popleft()
            
            if curr == n * n:
                return rolls
                
            for i in range(1, 7):
                next_sq = curr + i
                if next_sq > n * n:
                    break
                    
                r, c = get_coordinates(next_sq)
                
                if board[r][c] != -1:
                    dest = board[r][c]
                else:
                    dest = next_sq
                    
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, rolls + 1))
                    
        return -1