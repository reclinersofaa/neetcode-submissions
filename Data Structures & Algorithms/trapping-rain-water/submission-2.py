class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        lmax = [0]*len(height)
        rmax = [0]*len(height)
        res = 0

        lmax[0] = height[0]
        for i in range(1, len(height)):
            lmax[i] = max(lmax[i - 1], height[i])
        
        rmax[len(height) - 1] = height[len(height) - 1]
        for j in range(len(height) - 2, -1, -1):
            rmax[j] = max(rmax[j + 1], height[j])

        for i in range(len(height)):
            res += min(rmax[i], lmax[i]) - height[i]

        return res


