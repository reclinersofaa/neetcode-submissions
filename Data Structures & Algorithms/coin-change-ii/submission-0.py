class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # amount, index : total combos or wtv

        def calc(amt, i): #amt is the current amount
            if (amt, i) in memo:
                return memo[(amt, i)]
            if amt == 0:
                return 1 #we hit a success combo 
            if i >= len(coins) or amt < 0:
                return 0 #we hit a fail combo
            
            memo[(amt, i)] = calc(amt - coins[i], i) + calc(amt, i + 1) #take and repeat + skip
            return memo[(amt, i)]

        return calc(amount, 0)