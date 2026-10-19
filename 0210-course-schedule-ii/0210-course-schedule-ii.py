class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        ind = defaultdict(list)
        for (a,b) in prerequisites:
            ind[a].append(b)
            ind[b]
        if numCourses == 1:
            return [0]
        if not prerequisites:
            k = []
            for i in range(numCourses):
                k.append(i)
            return k
        print(ind)
        safe = set()
        order = []
        def search(st, visited):
            print(st)
            if st not in ind:
                order.append(st)
                return True
            if st in safe:
                return True
            if st in visited:
                return False
            visited.add(st)
            for k in ind[st]:
                a = search(k,visited)
                if a == False:
                    return False
            visited.remove(st)
            
            safe.add(st)
            order.append(st)
            return True
        for p in range(numCourses):
            a = search(p,set())
            if a == False:
                return []
        print(safe)
        return order
        