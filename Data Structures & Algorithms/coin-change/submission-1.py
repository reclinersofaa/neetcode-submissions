class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def calc(amount):
            mncoins = float('inf')
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            for coin in coins:
                if amount - coin >= 0:
                    mncoins = min(mncoins, 1 + calc(amount - coin))
                
            memo[amount] = mncoins
            return memo[amount]
            
        mincoins = calc(amount)
        return -1 if mincoins == float('inf') else mincoins