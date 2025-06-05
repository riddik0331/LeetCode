class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            cur_price = prices[i]
            cur_profit = cur_price - min_price
            if cur_price < min_price:
                min_price = cur_price
            elif cur_profit > profit:
                profit = cur_profit
        return profit
