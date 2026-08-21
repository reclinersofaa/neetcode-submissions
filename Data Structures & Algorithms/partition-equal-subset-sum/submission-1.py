class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums)/2
        memo = {} #store (index, target):true/false

        def dfs(i, target):
            if target == 0:
                return True
            if i == len(nums) or target < 0:
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            
            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            #the choice between including or excluding 

            return memo[(i, target)]
        
        return dfs(0, target)