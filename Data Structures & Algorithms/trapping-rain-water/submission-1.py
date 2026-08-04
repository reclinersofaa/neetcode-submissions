class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0

        for i in range(len(height)):
            lmax = rmax = height[i]

            for j in range(i + 1, len(height)):
                rmax = max(rmax, height[j])
            
            for k in range(i):
                lmax = max(lmax, height[k])
            
            res += min(lmax, rmax) - height[i]
        
        return res


        
        

