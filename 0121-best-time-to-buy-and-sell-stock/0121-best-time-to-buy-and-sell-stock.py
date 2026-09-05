class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left , right = 0 , 1
        mp = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            elif prices[left] <= prices[right]:
                mp = max((prices[right] - prices[left]) , mp)
                right += 1
        return mp