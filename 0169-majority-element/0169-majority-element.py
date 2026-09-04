class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = {}
        for i in range(len(nums)):

            di[nums[i]] = di.get(nums[i] , 0)+1

        for k,v in di.items():
            if v > len(nums)//2:
                return k

        
            
            