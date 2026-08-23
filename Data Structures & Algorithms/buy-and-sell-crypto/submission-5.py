class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 100
        sell = 0
        profit = 0
        for i in range(len(prices)):
            k = prices[i]
            buy = min(buy , k)
            sell = k
            profit = max (profit , sell - buy)
        return profit