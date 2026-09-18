class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        ma = {}
        for i in range(len(board)):
            curr = board[i]
            for j in range(len(curr)):
                val = board[i][j]
                if val == ".":
                    continue
                if val in ma:
                    if f'in row {i}' in ma[val] or f'in col {j}' in ma[val] or f'in bracket {i//3} and {j//3}' in ma[val]:
                        print(ma)
                        print(i,j)
                        print(val)
                        return False
                    else:
                        lis = ma.get(val,[])
                        poi=f'in row {i}'
                        poj=f'in col {j}'
                        sqr=f'in bracket {i//3} and {j//3}'
                        lis.append(poi)
                        lis.append(poj)
                        lis.append(sqr)
                        ma[val] = lis
                    
                else:
                    lis = ma.get(val,[])
                    poi=f'in row {i}'
                    poj=f'in col {j}'
                    sqr=f'in bracket {i//3} and {j//3}'
                    lis.append(poi)
                    lis.append(poj)
                    lis.append(sqr)
                    ma[val] = lis
        print(ma)
        return True