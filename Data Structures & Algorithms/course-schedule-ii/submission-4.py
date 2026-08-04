class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseRel = defaultdict(list)
        activepath = set()
        visited = set()
        res = []

        for p in prerequisites:
            courseRel[p[0]].append(p[1])
        
        def dfs(crs):
            if crs in activepath:
                return False
            if crs in visited:
                return True
            
            activepath.add(crs)
            for c in courseRel[crs]:
                if not dfs(c): return False

            activepath.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return res
