class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        farthest = 0
        jumps = 0

        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i]) #where will the window take you the furthest (jump index = curr index + jump value)
            jumps += 1
            l = r + 1
            r = farthest
        
        return jumps
                