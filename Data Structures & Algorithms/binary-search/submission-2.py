class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mean = (l + r)//2

            if nums[mean] < target:
                l = mean + 1
            elif nums[mean] > target:
                r = mean - 1
            elif nums[mean] == target:
                return mean

        return -1
        

        
