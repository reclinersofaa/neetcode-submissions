import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,zc = 1,0
        for i in nums:
            if i:
                prod *= i
            else:
                zc += 1
        
        if zc > 1: return len(nums)*[0]

        res = len(nums)*[0]
        for i,c in enumerate(nums):
            if zc:
                if c: res[i] = 0 
                else: res[i] = prod
            else:
                res[i] = prod//c
        
        return res