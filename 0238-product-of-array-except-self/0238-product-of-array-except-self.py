import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        n = len(nums)
        left = 1
        for i in range(n):
            res[i]= left
            left *= nums[i]
        right = 1
        for j in range(n-1, -1, -1):
            res[j] *= right 
            right *= nums[j]
        return res
        
                