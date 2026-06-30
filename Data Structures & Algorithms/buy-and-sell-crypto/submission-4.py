class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        #  l  r
        # [7, 1, 5, 3, 6, 4]
        l = 0
        r = 1 
        maxProf = 0

        while r < len(prices): # 0 < 1
            if prices[r] > prices[l]:
                currSum = prices[r] - prices[l] # currSum = 5 - 1 = 4
                maxProf = max(maxProf, currSum) # maxProf = max(0, -6)
            else:
                l = r
            r += 1
        return maxProf




