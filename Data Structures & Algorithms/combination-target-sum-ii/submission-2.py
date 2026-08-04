class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        sub = []
        def dfs(i, target):
            if target < 0:
                return 

            if target == 0:
                res.append(sub.copy())
                return 
            
            if i >= len(nums):
                return 
            
            sub.append(nums[i])
            dfs(i + 1, target - nums[i])

            sub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, target)
        
        dfs(0, target)
        return res