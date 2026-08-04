class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxd = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                diff = prices[r] - prices[l]
                maxd = max(maxd, diff)
                r += 1
            
        return maxd