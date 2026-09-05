class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pft = 0
        left , right = 0 , 1
        while right<len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            elif prices[right] > prices[left]:
                pft += prices[right] - prices[left]
                right += 1
                left += 1
            else:
                right += 1
                left += 1
        return pft