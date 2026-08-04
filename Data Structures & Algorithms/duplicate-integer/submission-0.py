class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in nums[0:n-1]:
            x = nums.index(i)
            for j in nums[x+1:]:
                print(i,j)
                if i == j:
                    return True
        return False