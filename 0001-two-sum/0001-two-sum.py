class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            curr = nums[i]
            t = target - curr
            for j in range(i+1,len(nums)):
                if nums[j] == t:
                    return [i,j]