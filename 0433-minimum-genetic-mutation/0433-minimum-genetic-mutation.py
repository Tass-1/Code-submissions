from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        def search():
            visited = set()
            queue = deque([(startGene, 0)])
            while queue:
                st , r = queue.popleft()
                if st == endGene:
                    return r
                for i in range(len(st)):
                    tmp = st[i]
                    for k in ("A", "C", "G", "T"):
                        if st[i] == k:
                            continue
                        new = st[:i] + k + st[i+1:]
                        print(new)
                        if new in bank and new not in visited:
                            print("found a match")
                            visited.add(new)
                            new = st[:i] + k + st[i+1:]
                            queue.append((new, r+1))
                        
            return -1
        g = search()
        return g
                        
                        
