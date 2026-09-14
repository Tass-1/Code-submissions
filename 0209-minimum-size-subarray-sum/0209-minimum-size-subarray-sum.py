class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minlen = float('inf')
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            while t >= target:
                minlen = min(minlen,i-left + 1)
                t -= nums[left]
                left += 1

        if minlen == float('inf'):
            return 0
        else:
            return minlen