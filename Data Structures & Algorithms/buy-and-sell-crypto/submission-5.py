class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: # [7, 1, 5, 3, 6, 4] expected = 5
            return 0        #     l  r
        
        l = 0
        r = 1
        maxProf = 0

        while r < len(prices): # l = 0, r = 1
            if prices[r] > prices[l]: # 5 > 1 ?
                maxProf = max(maxProf, prices[r] - prices[l]) # maxProf = 4
                #l += 1
            else:
                l = r
            r += 1
        return maxProf



