class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def calc(t, i):
            if (t, i) in memo:
                return memo[(t, i)]
            if t == 0 and i == len(nums):
                return 1
            if t and i == len(nums):
                return 0
            
            memo[(t, i)] = calc(t - nums[i], i + 1) + calc(t + nums[i], i + 1)
            return memo[(t, i)]
        
        return calc(target, 0)