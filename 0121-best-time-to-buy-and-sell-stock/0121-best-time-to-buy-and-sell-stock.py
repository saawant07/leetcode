class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        profit = 0

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                profit = max(profit, price - minimum)

        return profit