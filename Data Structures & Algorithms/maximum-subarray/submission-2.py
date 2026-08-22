class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        csum = nums[0]

        for i in nums[1:]:
            csum = max(i, csum + i)
            res = max(res, csum)
        
        return res
    
