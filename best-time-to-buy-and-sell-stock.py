class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = iter(prices)
        buy_price = next(prices)
        max_profit = 0
        for current_price in prices:
            max_profit = max(current_price - buy_price, max_profit)
            buy_price = min(buy_price, current_price)
        return max_profit
