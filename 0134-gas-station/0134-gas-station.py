class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        k = []
        res = 0
        
        for j in range(len(cost)):
            t = gas[j] -cost[j]
            k.append(t)
        if sum(k) < 0:
            return -1
        i = 0
        b = 0
        bd = False
        offset = 0
        tank = 0
        while b <= (len(cost)):
            idx = i % len(cost)
            diff = k[idx]
            tank += diff
            if tank <0:
                tank = 0
                i += 1
                if bd == True:
                    offset =b
                    bd = False
                continue
            res = idx
            b+=1
            bd = True
            i += 1
        print(tank)
        if tank < 0:
            return -1
        else:
            return res + offset