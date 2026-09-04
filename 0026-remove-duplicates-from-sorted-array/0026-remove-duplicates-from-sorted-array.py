class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        di = []
        while i < len(nums):
            curr = nums[i]
            if curr in di:
                nums.pop(i)
            else:
                di.append(curr)
                i += 1
        return len(nums)