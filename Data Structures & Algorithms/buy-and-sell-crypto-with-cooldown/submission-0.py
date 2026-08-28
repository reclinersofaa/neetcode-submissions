class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # {(choice (1 - Bought, 0 - Not Bought), index) : max money possible at that day

        def calc(choice, i):
            if (choice, i) in memo:
                return memo[(choice, i)]
            
            if i >= len(prices):
                return 0

            if choice: #bought, stock in hand (remember cooldown period - +2 index)
                sell = prices[i] + calc(0, i + 2) 
                skip = calc(1, i + 1)
                memo[(choice, i)] = max(sell, skip)
            if not choice: #not bought, no stock in hand
                buy = -prices[i] + calc(1, i + 1)
                skip = calc(0, i + 1)
                memo[(choice, i)] = max(buy, skip)

            return memo[(choice, i)]

        return calc(0, 0)
