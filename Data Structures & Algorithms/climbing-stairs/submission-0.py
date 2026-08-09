class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climber(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            res = climber(n - 1) + climber(n - 2)
            memo[n] = res
            return res
        
        return climber(n)

        
