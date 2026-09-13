class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0
        
        while left < right:
            lh = height[left]
            rh = height[right]
            if lh <= rh:
                area = min(lh,rh) * (right-left)
                res = max(res,area)
                left += 1
            elif rh <= lh:
                area = min(lh,rh) * (right-left)
                res = max(res,area)
                right -= 1
            

        return res

            

