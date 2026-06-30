class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 
        profit = 0

        while r < len(prices):
            if prices[r] > prices[l]: # check for profitability
                profit = max(profit, prices[r] - prices[l])

            elif prices[l] > prices[r]: # invalid state
                l = r
            r += 1
        return profit



