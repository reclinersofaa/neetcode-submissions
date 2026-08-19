class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        res = 0

        def dfs(i):
            if i in memo:
                return memo[i]
            
            submax = 1 #every number itself is a subsequence of 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    submax = max(submax, 1 + dfs(j))
            
            memo[i] = submax
            return memo[i]
        
        for i in range(len(nums)):
            res = max(res, dfs(i))
        
        return res