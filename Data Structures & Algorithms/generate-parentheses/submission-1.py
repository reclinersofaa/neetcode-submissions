class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        sub = []
        def dfs(o, c):
            if len(sub) == 2*n:
                res.append(''.join(sub))
                return 
            
            if n > o:
                sub.append('(')
                dfs(o + 1, c)
                sub.pop()
            
            if o != c:
                sub.append(')')
                dfs(o, c + 1)
                sub.pop()
        
        dfs(0, 0)
        return res