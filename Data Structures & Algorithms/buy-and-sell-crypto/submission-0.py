class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxd = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                maxd = max(maxd, prices[j] - prices[i])
        
        return maxd
