class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = 0
        for i in range(len(nums)):
            if i > t:
                return False
            t = max(t , i+ nums[i])
            if t > len(nums)-1:
                return True
        return True
        
       
