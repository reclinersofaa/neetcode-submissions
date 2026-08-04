class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseRel = defaultdict(list)
        activepath = set()

        for i in range(len(prerequisites)):
            courseRel[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(crs):
            if crs in activepath:
                return False
            if courseRel[crs] == []:
                return True
            
            activepath.add(crs)
            for c in courseRel[crs]:
                if not dfs(c):
                    return False
            activepath.remove(crs)
            courseRel[crs] = []
            return True
        
        for p in prerequisites:
            if not dfs(p[0]): return False
        return True
            
        

        

        
