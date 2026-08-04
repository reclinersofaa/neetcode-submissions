class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sub = []
        nums.sort()
        def dfs(i):
            if sum(sub) > target:
                return 

            if sum(sub) == target:
                res.append(sub.copy())
                return 
            
            if i >= len(nums):
                return 
            
            sub.append(nums[i])
            dfs(i + 1)

            sub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return res