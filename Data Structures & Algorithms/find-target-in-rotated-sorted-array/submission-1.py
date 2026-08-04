class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if target == nums[mid]:
                return mid
            elif nums[r] > nums[mid]: #mid associated with right /
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: #mid associated with left ^ 
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1