class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #in the case theres only 1 negative element, so dont use 0
        cmax, cmin = 1, 1

        for n in nums:
            if n == 0:
                cmax, cmin = 1, 1 #with assigning 1, dont carry over prev accumulations after 0
                continue 
            
            tmp = n * cmax #cause cmax will be updated later
            cmax = max(n * cmax, n * cmin, n) 
            cmin = min(tmp, n * cmin, n)
            
            res = max(cmax, res)
        
        return res

#Me notes:           
#cmax calculates the max at that point in time, be it with a currently positive number (n * cmax), negative number (n * cmin) OR n itself

#cmin calculates the min in a similar way