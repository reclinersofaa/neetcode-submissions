class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sr = ''.join(sorted(s))
        tr = ''.join(sorted(t))
        if sr == tr:
            return True
        else:
            return False