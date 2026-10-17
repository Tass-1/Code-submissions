from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        ind = defaultdict(list)
        for (a,b) in prerequisites:
            ind[a].append(b)
        if numCourses == 1 or not prerequisites:
            return True
        print(ind)
        safe = set()
        def search(st,en, visited):
            if st not in ind:
                return True
            if st in safe:
                return True
                
            if st not in ind:
                return True
            if st in visited:
                return False
            if st in visited:
                return False
            visited.add(st)
            for k in ind[st]:
                a = search(k,en,visited)
                if a == False:
                    return False
            visited.remove(st)
            safe.add(st)
            return True
        for p in prerequisites:
            a = search(p[1], p[0], set())
            if a == False:
                return False
        return True
        
        
