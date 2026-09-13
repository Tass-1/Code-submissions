class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        left = 0
        right = len(nums)-1
        res = set()
        while left < right:
            nect = left + 1
            right = len(nums)-1
            while nect < right:
                lh = nums[left]
                rh = nums[right]
                nh = nums[nect]
                sum = rh + lh + nh
                if sum == 0:
                    res.add((lh,nh,rh))
                    nect += 1
                    right -= 1
                    
                elif sum > 0:
                    right -= 1
                else:
                    nect += 1
            left += 1
        return [list(k) for k in res]
