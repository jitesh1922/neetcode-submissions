class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 1000
        profit = 0
        for i in range(0, len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            else:
                profit = max(profit, (prices[i] - mini))
            
        return profit