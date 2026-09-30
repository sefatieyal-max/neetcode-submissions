class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        while (left < len(prices)-1) and right < len(prices):
            buy = prices[left]
            sell = prices[right]
            profit = sell - buy
            max_profit = max(profit,max_profit)
            if buy > sell:
                left = right
            else:
                right += 1
        return max_profit

