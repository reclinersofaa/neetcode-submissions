class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited, prevheight):
            if ((r, c) in visited  
                or r not in range(rows) or c not in range(cols)
                or heights[r][c] < prevheight):
                return
            visited.add((r, c)) #if the prevheight is smaller, then the neighbour will flow into the prev tile which will defo flow into ocean because continuous chain of calls
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        return [list(coord) for coord in pac & atl]
