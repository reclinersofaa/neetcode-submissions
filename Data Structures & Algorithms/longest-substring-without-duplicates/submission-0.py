class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hs = set()
        maxi = 0

        while r < len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            maxi = max(maxi, r - l + 1)
            r += 1
        return maxi