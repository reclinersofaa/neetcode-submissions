class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        fin = 0

        for n in nums:
            if n - 1 not in hset: #check if ele not the first in sequence
                curr = n
                len = 0
                while curr in hset: #iterate through sequence just by increment
                    curr += 1
                    len += 1
                if len > fin:
                    fin = len
        
        return fin
