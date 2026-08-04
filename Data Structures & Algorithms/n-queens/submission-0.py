class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pd = set()
        nd = set()

        res = []
        board = [["."]*n for i in range(n)]

        def dfs(r):
            if r == n: #end of scenario, all rows done
                copy = ["".join(row) for row in board] #list of each row as a string
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r - c) in nd or (r + c) in pd:
                    continue
                
                cols.add(c) 
                pd.add(r + c)
                nd.add(r - c)

                board[r][c] = "Q" #change and advance with branch
                dfs(r + 1)

                cols.remove(c) #reset for backtracking
                pd.remove(r + c)
                nd.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res         
