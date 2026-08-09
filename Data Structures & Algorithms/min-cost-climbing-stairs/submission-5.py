class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def calc(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(calc(i - 1), calc(i - 2))
            return memo[i]
        
        n = len(cost)
        return min(calc(n - 1), calc(n - 2))
            