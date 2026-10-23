class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
    
        def search(ip,path):
            if len(path) == k:
                print(path)
                result.append(path.copy())
                return
            if ip > n:
                return 
            num = ip
            for p in range(ip,n+1):
                path.append(p)
                search(p+1,path)
                path.pop()

        search(1,[])
        return result