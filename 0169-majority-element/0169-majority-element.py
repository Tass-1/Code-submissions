class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        di = {}
        for i in range(len(nums)):
            curr = nums[i]
            di[curr] = di.get(curr , 0)+1
        re = []
        for k,v in di.items():
            if v > n:
                return k
                break
        
            
            