class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)

        fin = 0
        for num in hset:
            if num - 1 not in hset:
                curr = num
                len = 0
                while curr in hset:
                    len += 1
                    curr += 1
                    print(num, curr, len)
                if fin < len:
                    fin = len
        return fin

        