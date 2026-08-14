class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def calc(i):
            ways = 0
            if i in memo: #if tracked in memo
                return memo[i]
            if i == len(s): #if reached end
                return 1
            if s[i] == "0": #skip the 0s
                return 0
            ways += calc(i + 1) #executes when its not 0
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26 : #if we could get greedy
                ways += calc(i + 2)

            memo[i] = ways
            return ways
        
        return calc(0)
        
        