class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -2
        lm = height[0]
        rm = height[len(height) -1]
        total = 0
        while left <= right:
            l = height[left]
            r = height[right]
            rm = max(rm , r)
            lm = max(lm , l)
            if l <= rm:
                if l < lm:
                    total += lm - l
                left += 1
            elif r <= lm:
                if r < rm:
                    total += rm -r
                right -= 1
            else:
                print("err")
        


        return total