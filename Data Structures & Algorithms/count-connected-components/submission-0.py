class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        AdjList = defaultdict(list)
        visited = set()
        count = 0

        for e in edges:
            AdjList[e[0]].append(e[1])
            AdjList[e[1]].append(e[0])
        
        def dfs(v):
            if v in visited: 
                return
            visited.add(v)
            for nei in AdjList[v]:
                dfs(nei)

        for ve in range(n):
            if ve not in visited:
                count += 1
                dfs(ve)
        
        return count
