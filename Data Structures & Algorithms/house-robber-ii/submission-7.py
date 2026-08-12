class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0] if len(nums) == 1 else 0

        memo1, memo2 = {}, {}
        arrwfirst = nums[1:]
        arrwlast = nums[:-1]

        def robber(i, arr, memo):
            if i < 0: return 0
            if i == 0: return arr[0]
            if i in memo: return memo[i]

            memo[i] = max(arr[i] + robber(i - 2, arr, memo), robber(i - 1, arr, memo))
            return memo[i]
        
        nwf = len(arrwfirst)
        nwl = len(arrwlast)

        reswf = robber(nwf - 1, arrwfirst, memo1)
        reswl = robber(nwl - 1, arrwlast, memo2)

        return max(reswf, reswl)

            
        



