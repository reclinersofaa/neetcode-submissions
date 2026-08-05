class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        for i in range(len(edges)):
            parent[i + 1] = i + 1
        
        def find(node):
            if parent[node] != node:
                return find(parent[node])
            return node
        
        def union(n1, n2):
            if n1 == n2:
                return False #cycle condition
            parent[n1] = n2
            return True
        
        for e in edges:
            if not union(find(e[0]), find(e[1])):
                return e
        return False

