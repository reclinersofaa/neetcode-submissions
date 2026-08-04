class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxsell = 0
        
        while (r < len(prices)):
            print(l, r)
            if prices[l] > prices[r]: l = r
            else: maxsell = max(maxsell, prices[r] - prices[l])
            r += 1
        
        return maxsell