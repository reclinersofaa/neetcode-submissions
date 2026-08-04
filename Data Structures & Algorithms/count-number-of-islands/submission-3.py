class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                ro, co = q.popleft()
                
                for (dr, dc) in directions:
                    nr, nc = ro + dr, co + dc
                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] == "1" and 
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands
