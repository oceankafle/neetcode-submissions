class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maintain the rule that left ALWAYS has to be before right
        l, r = 0, 1
        overall_best = 0 # global variable

        # [1, 10, 5, 6, 7]

        while r < len(prices):
            curr_best = prices[r] - prices[l]
            overall_best = max(overall_best, curr_best)

            if prices[l] > prices[r]: # means we're in a negative state, bad
                l = r
                r += 1
            else:
                r += 1
        return overall_best

        

        # prices = [10, 1, 5, 6, 7, 1]

        # buy on day 0, sell on day 1
        # 1 - 10 = -9 profit (bad)
        # 
