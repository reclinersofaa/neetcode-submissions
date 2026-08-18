class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} #store true or false at that particular index

        def dfs(i):
            if i == len(s): return True
            if i in memo: return memo[i]

            for w in wordDict:
                r = i + len(w) 
                if r <= len(s) and s[i:r] == w:
                    if dfs(r):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]
        
        return dfs(0)