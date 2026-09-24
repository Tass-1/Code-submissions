class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        i = 0
        while i < len(nums):
            curr = nums[i]
            temp = [curr, curr]
            val = curr
            j = i+1
            while j <len(nums):
                if nums[j] == val +1:
                    val += 1
                    temp[1] = val
                    j+=1
                else:
                    i = j
                    ranges.append(temp)
                    
                    break
            if j > len(nums)-1:
                ranges.append(temp)
                break
        res = []
        for i in range(len(ranges)):
            curr = ranges[i]
            if curr[0] == curr[1]:
                k = "".join(f"{curr[0]}")
                res.append(k)
            else:
                tp = "".join(f"{curr[0]}->{curr[1]}") 
                res.append(tp)
        print(res)
        return res