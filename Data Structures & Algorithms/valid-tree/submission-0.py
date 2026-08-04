class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        AdjList = defaultdict(list)
        visited = set()

        for e in edges:
            AdjList[e[0]].append(e[1])
            AdjList[e[1]].append(e[0])
        
        def dfs(v, p):
            if v in visited:
                return False
            visited.add(v)
            for n in AdjList[v]:
                if n != p: 
                    if not dfs(n, v): return False
            return True
        
        if dfs(0, -1):
            return len(visited) == n
        return False
             