class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hset = set()
        length = 0

        while (r < len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            length = max(length, r - l + 1)
            r += 1

        return length