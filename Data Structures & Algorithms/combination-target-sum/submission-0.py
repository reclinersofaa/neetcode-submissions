class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sub = []
        def dfs(i):
            if sum(sub) > target:
                return 
                
            if sum(sub) == target:
                res.append(sub.copy())
                return 
            
            if i >= len(nums):
                return 
        
            sub.append(nums[i])
            dfs(i)

            sub.pop()
            dfs(i + 1)
        
        dfs(0)
        return res