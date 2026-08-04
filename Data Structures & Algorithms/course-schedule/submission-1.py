class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseRel = defaultdict(list)
        activepath = set()

        for i in range(len(prerequisites)):
            courseRel[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(crs):
            if crs in activepath: #cycle detected
                return False
            if courseRel[crs] == []: #no prerequisites
                return True
            
            activepath.add(crs) 
            for c in courseRel[crs]: #go through each prerequisite, then dfs for each
                if not dfs(c):
                    return False #if any prerequisite branch turns out to have cycle 
            activepath.remove(crs) 
            courseRel[crs] = [] #optimization for revisits
            return True
        
        for p in prerequisites: #in the case we have disjoint graph
            if not dfs(p[0]): return False
        return True
            
        

        

        
