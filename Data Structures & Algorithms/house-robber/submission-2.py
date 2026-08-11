class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def robber(i):
            if i < 0: return 0
            if i == 0: return nums[0]
            if i in memo: return memo[i]

            memo[i] = max(nums[i] + robber(i - 2), robber(i - 1))
            return memo[i]
        
        n = len(nums)
        return max(robber(n - 1), robber(n - 2))