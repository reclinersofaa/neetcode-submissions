class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            iarea = 1

            q.append((r, c))
            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                (ro, co) = q.popleft()
                for (dr, dc) in directions:
                    nr, nc = ro + dr, co + dc
                    if ((nr in range(rows)) and (nc in range(cols))  
                        and ((nr, nc) not in visited)  
                        and grid[nr][nc] == 1):
                        iarea += 1
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
            return iarea
                   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, bfs(r, c))
        
        return area



